import asyncio
import logging

import numpy as np
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from tensorflow.keras.models import load_model

from config import spawnlogconfirm, starchconfirm
from constants import COLOR_RARE, COLOR_REGIONAL
import spawn_embeds
import cmd_embeds
import pokedex
import preprocess_image
import star_helper
import spawn_logger

log = logging.getLogger(__name__)

# TensorFlow takes upwards of ten seconds to load the model and says nothing
# while it does, which reads as a hang. flush because the import blocks after.
print("loading recognition model, this takes a few seconds...", flush=True)
loaded_model = load_model('data/model.h5', compile=False)

# tier -> (spawn phrase, spawn colour, starboard label)
TIERS = {
    'mythic': ('A mythic Pokemon spawned!', COLOR_RARE, 'It is a Mythic Pokémon!'),
    'legendary': ('A legendary Pokemon spawned!', COLOR_RARE, 'It is a Legendary Pokémon!'),
    'ub': ('An Ultra Beast spawned!', COLOR_RARE, 'It is an Ultra Beast Pokémon!'),
    'regional': ('A regional Pokémon spawned!', COLOR_REGIONAL, 'It is a Regional Pokémon!'),
}


async def identify(session, url):
  """Download an image and return the predicted Pokémon name, or None on failure."""
  try:
    async with session.get(url=url) as resp:
      if resp.status != 200:
        log.warning("image fetch failed: HTTP %s for %s", resp.status, url)
        return None
      content = await resp.read()
  except (OSError, asyncio.TimeoutError) as exc:
    log.warning("image fetch errored for %s: %s", url, exc)
    return None

  try:
    # convert('RGB') drops any alpha channel; the model takes 3 channels.
    image = Image.open(BytesIO(content)).convert('RGB')
  except UnidentifiedImageError:
    log.warning("not a decodable image: %s", url)
    return None

  preprocessed = preprocess_image.pimg(image)
  # Inference is a blocking C call. Run it off the event loop or every spawn
  # freezes the bot's heartbeat for the duration.
  predictions = await asyncio.to_thread(loaded_model, preprocessed, training=False)
  index = int(np.argmax(np.asarray(predictions), axis=1)[0])
  return pokedex.index_to_name[index]


async def outnmodule(bot, message, url):
  name = await identify(bot.http_session, url)
  if name is None:
    return

  if spawnlogconfirm:
    await spawn_logger.logthespawn(bot, message, name)

  tier = pokedex.tier_of(name)
  if tier == 'common':
    await spawn_embeds.spawn_embed(message, name)
    return

  phrase, color, label = TIERS[tier]
  ping = (spawn_embeds.regional_ping() if tier == 'regional'
          else spawn_embeds.rare_ping())
  await spawn_embeds.spawn_embed(message, name, phrase, color, ping)

  if starchconfirm:
    await star_helper.starit(bot, message, name, label, color)


async def identifycmd(bot, message, url):
  name = await identify(bot.http_session, url)
  if name is None:
    await message.channel.send("Couldn't read that image.")
    return
  await cmd_embeds.identify_embed(message, name)
