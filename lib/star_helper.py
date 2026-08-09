import logging

import discord
from discord import Embed

from config import starch
from constants import COLOR_RARE, FOOTER, POKETWO_AVATAR

log = logging.getLogger(__name__)


async def starit(bot, message, name, label, color=COLOR_RARE):
  """Mirror a rare spawn into the starboard channel.

  `label` is the tier headline, e.g. 'It is a Mythic Pokémon!'.
  """
  starboard = bot.get_channel(starch)
  if starboard is None:
    return

  og_embed = message.embeds[0]
  staryu = Embed(color=color)
  staryu.set_author(name="Pokétwo", icon_url=POKETWO_AVATAR)
  staryu.add_field(name=og_embed.title, value=og_embed.description, inline=False)
  staryu.add_field(name='',
                   value=f'[Jump to Message]({message.jump_url})', inline=False)
  staryu.add_field(name=label, value=f'It is **__{name}__** !', inline=False)
  staryu.set_image(url=og_embed.image.url)
  staryu.set_footer(text=FOOTER)

  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")

  # Marks the spawn itself, so it stays obvious which message was starred
  # after the confirmation scrolls away.
  try:
    await message.add_reaction('⭐')
  except discord.HTTPException:
    # Missing Add Reactions permission shouldn't lose the starboard post.
    log.warning("could not react to %s", message.jump_url)
