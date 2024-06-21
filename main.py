#imports
import aiohttp
import aiosqlite
import asyncio
import configparser

import json
import os

import discord
from discord.ext import commands

import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from io import BytesIO

#OutN version
version = 'v3.1'

#user inputs
config = configparser.ConfigParser()
config_file = 'config.ini'

def get_config():
  if not os.path.exists(config_file):
    token = input("Enter your Discord bot token: ")
    rping = input("Enter the role ID for rare ping: ")

    config['DEFAULT'] = {'TOKEN': token, 'RPING': rping}

    with open(config_file, 'w') as configfile:
      config.write(configfile)
  else:
    config.read(config_file)

get_config()

TKN = config['DEFAULT']['TOKEN']
rping = int(config['DEFAULT']['RPING'])

#bot setup
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='~', intents=intents)

#data load
loaded_model = load_model('model.h5', compile=False)

with open('classes.json', 'r') as f:
  classes = json.load(f)

with open('data/trares.txt', 'r') as file:
  rares = file.read()

with open('data/legendary.txt', 'r') as file:
  legendary_list = file.read()

with open('data/mythical.txt', 'r') as file:
  mythical_list = file.read()

with open('data/ultrabeast.txt', 'r') as file:
  ub_list = file.read()


#custom modules
async def mythic_embed(message, name):
  embed = discord.Embed(color=discord.Color.gold())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(
      name='New Spawn!',
      value=
      f'**__{name}__**, A mythic Pokemon spawned! catch it using:')
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)

async def legendary_embed(message, name):
  embed = discord.Embed(color=discord.Color.gold())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(
      name='New Spawn!',
      value=
      f'**__{name}__**, A legendary Pokemon spawned! catch it using:'
  )
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)

async def ub_embed(message, name):
  embed = discord.Embed(color=discord.Color.gold())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(
      name='New Spawn!',
      value=
      f'**__{name}__**, An Ultra Beast spawned! catch it using:'
  )
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)

async def common_embed(message, name):
  embed = discord.Embed(color=discord.Color.blue())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(
      name='New Spawn!',
      value=f'**__{name}__** spawned! catch it using:')
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)


@bot.event
async def on_ready():
  bot.db = await aiosqlite.connect("pokemon.db")
  await bot.db.execute("CREATE TABLE IF NOT EXISTS pokies (command str)")
  await bot.db.commit()

  print('Logged in as', bot.user)
  print("The OutN Project",version)

  game = discord.Game("Pokémon")
  await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message):
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
        preprocessed_image = await preprocess_image(image)
        predictions = loaded_model.predict(preprocessed_image)
        classes_x = np.argmax(predictions, axis=1)
        name = list(classes.keys())[classes_x[0]]
        async with message.channel.typing():
          if name in mythical_list:
            await mythic_embed(message, name)
            await message.channel.send(f"<@&{rping}>")

          elif name in legendary_list and name != 'natu':
            await legendary_embed(message, name)
            await message.channel.send(f"<@&{rping}>")

          elif name in ub_list:
            await ub_embed(message, name)
            await message.channel.send(f"<@&{rping}>")

          else:
            await common_embed(message, name)


async def preprocess_image(image):
  image = image.resize((64, 64))
  image = np.array(image)
  image = image / 255.0
  image = np.expand_dims(image, axis=0)
  return image


bot.run(TKN)
