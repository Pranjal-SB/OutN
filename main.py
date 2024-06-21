import aiosqlite
import configparser
import os

import discord
from discord.ext import commands

from makeconfig import TKN
from TheOutNModule import outnmodule

version = 'v4.0'

#user inputs
config = configparser.ConfigParser()
config_file = 'config.ini'

def get_config():
  if not os.path.exists(config_file):
    token = input("Enter your Discord bot token: ")
    rping = input("Enter the role ID for rare ping: ")
    regping = input("Enter the role ID for regional ping: ")
    config['DEFAULT'] = {'TOKEN': token, 'RPING': rping, 'REGPING': regping}

    with open(config_file, 'w') as configfile:
      config.write(configfile)
  else:
    config.read(config_file)

get_config()

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
