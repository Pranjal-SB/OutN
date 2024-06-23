import aiohttp
import json
import os
import platform

import numpy as np
from PIL import Image
from io import BytesIO
from tensorflow.keras.models import load_model

import embeds
import hint_helper
import star_helper
import preprocess_image

loaded_model = load_model('model.h5', compile=False)

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

with open('classes.json', 'r') as f:
  classes = json.load(f)

with open('data/legendary', 'r') as file:
  legendary_list = file.read()

with open('data/mythical', 'r') as file:
  mythical_list = file.read()

with open('data/ultrabeast', 'r') as file:
  ub_list = file.read()

with open('data/regional', 'r') as file:
  reg_list = file.read()


async def outnmodule(bot, message):
  if message.author.id == 716390085896962058:
    if len(message.embeds) > 0:
      embed = message.embeds[0]
      if "appeared!" in embed.title and embed.image:
        url = embed.image.url
        async with aiohttp.ClientSession() as session:
          async with session.get(url=url) as resp:
            if resp.status == 200:
              content = await resp.read()
              image_data = BytesIO(content)
              image = Image.open(image_data)
        preprocessed_image = await preprocess_image.pimg(image)
        predictions = loaded_model.predict(preprocessed_image)
        classes_x = np.argmax(predictions, axis=1)
        name = list(classes.keys())[classes_x[0]]

        if name in mythical_list:
          await embeds.mythic_embed(message, name)
          await star_helper.starit_mythic(bot, message, name)

        elif name in legendary_list and name != 'natu':
          await embeds.legendary_embed(message, name)
          await star_helper.starit_legen(bot, message, name)

        elif name in ub_list:
          await embeds.ub_embed(message, name)
          await star_helper.starit_ub(bot, message, name)

        elif "galar" in name or "alola" in name or "hisui" in name or name in reg_list:
          await embeds.reg_embed(message, name)
          await star_helper.starit_reg(bot, message, name)

        else:
          await embeds.common_embed(message, name)

    elif 'The pokémon is ' in message.content:
      for i in hint_helper.solve(message.content):
        await embeds.hint_embed(i, message)
        
  elif 'The pokémon is ' in message.content:
    for i in hint_helper.solve(message.content):
      await embeds.hint_embed(i, message)
