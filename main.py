import asyncio
import configparser
import json
import os
from io import BytesIO

import aiohttp
import aiosqlite
import discord
import numpy as np
from discord.ext import commands
from PIL import Image
from tensorflow.keras.models import load_model

config = configparser.ConfigParser()
config_file = 'config.ini'


def get_config():
  if not os.path.exists(config_file):
    token = input("Enter your Discord bot token: ")
    rping = input("Enter the role ID for rping: ")

    config['DEFAULT'] = {'TOKEN': token, 'RPING': rping}

    with open(config_file, 'w') as configfile:
      config.write(configfile)
  else:
    config.read(config_file)


get_config()

TKN = config['DEFAULT']['TOKEN']
rping = int(config['DEFAULT']['RPING'])

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='~', intents=intents)
game = discord.Game("Pokémon")

loaded_model = load_model('model.h5', compile=False)

with open('classes.json', 'r') as f:
  classes = json.load(f)

with open('data/trares', 'r', encoding='utf8') as file:
  rares_list = file.read()

with open('data/legendary', 'r') as file:
  legendary_list = file.read()

with open('data/mythical', 'r') as file:
  mythical_list = file.read()


@bot.event
async def on_ready():
  bot.db = await aiosqlite.connect("pokemon.db")
  await bot.db.execute("CREATE TABLE IF NOT EXISTS pokies (command str)")
  await bot.db.commit()
  print('Logged in as', bot.user)
  await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message):
  while not hasattr(bot, 'db'):
    await asyncio.sleep(0.1)
  if message.author.id == 716390085896962058 and len(message.embeds) > 0:
    embed = message.embeds[0]
    if "appeared!" in embed.title and embed.image:
      url = embed.image.url
      async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
          if resp.status == 200:
            content = await resp.read()
            image_data = BytesIO(content)
            image = Image.open(image_data)
      preprocessed_image = await preprocess_image(image)
      predictions = loaded_model.predict(preprocessed_image)
      classes_x = np.argmax(predictions, axis=1)
      name = list(classes.keys())[classes_x[0]]
      async with message.channel.typing():
        if name in rares_list:
          await message.channel.send(
              f"<@&{rping}> **__{name}__** is a rare pokemon! catch using:")
          await message.channel.send(f"@Pokétwo#8236 c {name}")
        else:
          await message.channel.send(f'**__{name}__** | catch using:')
          await message.channel.send(f"@Pokétwo#8236 c {name}")


async def preprocess_image(image):
  image = image.resize((64, 64))
  image = np.array(image)
  image = image / 255.0
  image = np.expand_dims(image, axis=0)
  return image


bot.run(TKN)
