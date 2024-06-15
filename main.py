import asyncio
import json
import random
from io import BytesIO

import aiohttp
import aiosqlite
import numpy as np
import discord
from discord.ext import commands
from PIL import Image
from tensorflow.keras.models import load_model


def get_token():
  try:
    with open('config', 'r') as f:
      return f.read().strip()
  except FileNotFoundError:
    token = input("Please enter your bot token: ").strip()
    with open('config', 'w') as f:
      f.write(token)
    return token


TOKEN = get_token()

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='on.', intents=intents)

loaded_model = load_model('model.h5', compile=False)
with open('classes.json', 'r') as f:
  classes = json.load(f)


@bot.event
async def on_ready():
  print('Logged in as', bot.user)
  bot.db = await aiosqlite.connect("pokemon.db")
  await bot.db.execute("CREATE TABLE IF NOT EXISTS pokies (command str)")
  print("pokies table created!!")
  await bot.db.commit()


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
        await asyncio.sleep(random.randint(3, 6))
        await message.channel.send(f"__**{name}**__ Spawned | catch using:")
        await message.channel.send(f"<@716390085896962058> c {name}")


async def preprocess_image(image):
  image = image.resize((64, 64))
  image = np.array(image)
  image = image / 255.0
  image = np.expand_dims(image, axis=0)
  return image


bot.run(TOKEN)
