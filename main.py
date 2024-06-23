import aiosqlite
import configparser
import os

import discord
from discord.ext import commands

from makeconfig import get_config
from TheOutNModule import outnmodule

version = 'v5.0'

#config
get_config()
config = configparser.ConfigParser()
config_file = 'config.ini'
config.read(config_file)

TKN = config['DEFAULT']['TOKEN']

#bot setup
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='on.', intents=intents)

@bot.event
async def on_ready():
  bot.db = await aiosqlite.connect("pokemon.db")
  await bot.db.execute("CREATE TABLE IF NOT EXISTS pokies (command str)")
  await bot.db.commit()
  print()
  print("The OutN Project",version)
  print("https://github.com/Pranjal-SB/OutN")
  print()
  print('Logged in as', bot.user)
  await bot.change_presence(status=discord.Status.online, activity=discord.Game("Pokémon"))

@bot.event
async def on_message(message):
  await outnmodule(bot, message)

bot.run(TKN)