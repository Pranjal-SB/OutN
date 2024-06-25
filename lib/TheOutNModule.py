import aiohttp
import json
import os
import platform
import configparser

import numpy as np
from PIL import Image
from io import BytesIO
from tensorflow.keras.models import load_model

import spawn_embeds
import preprocess_image
import star_helper
import spawn_logger

loaded_model = load_model('data/model.h5', compile=False)

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

with open('data/classes.json', 'r') as f:
  classes = json.load(f)

with open('data/pokes/legendary', 'r') as file:
  legendary_list = file.read()

with open('data/pokes/mythical', 'r') as file:
  mythical_list = file.read()

with open('data/pokes/ultrabeast', 'r') as file:
  ub_list = file.read()

with open('data/pokes/regional', 'r') as file:
  reg_list = file.read()


#config
config = configparser.ConfigParser()
config_file = 'config.ini'
config.read(config_file)

spawnlogconfirm = config['CONFIRMS']['SPAWNLOGCONFIRM']
starchconfirm = config['CONFIRMS']['STARCHCONFIRM']

async def outnmodule(bot, message, url):
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
  if spawnlogconfirm in 'Yy':
    await spawn_logger.logthespawn(bot, message, name)

  if name in mythical_list:
    await spawn_embeds.mythic_embed(message, name)
    if starchconfirm in 'Yy':
      await star_helper.starit_mythic(bot, message, name)

  elif name in legendary_list and name != 'natu':
    await spawn_embeds.legendary_embed(message, name)
    if starchconfirm in 'Yy':
      await star_helper.starit_legen(bot, message, name)

  elif name in ub_list:
    await spawn_embeds.ub_embed(message, name)
    if starchconfirm in 'Yy':
      await star_helper.starit_ub(bot, message, name)

  elif "galar" in name or "alola" in name or "hisui" in name or name in reg_list:
    await spawn_embeds.reg_embed(message, name)
    if starchconfirm in 'Yy':
      await star_helper.starit_reg(bot, message, name)

  else:
    await spawn_embeds.common_embed(message, name)
