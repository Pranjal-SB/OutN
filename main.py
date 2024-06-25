import aiosqlite
import configparser
import sys

import discord
from discord.ext import commands

sys.path.append('lib')
from makeconfig import get_config
from TheOutNModule import outnmodule
import hint_helper
import catch_helper

version = 'v7.0'

#config
get_config()

config = configparser.ConfigParser()
config_file = 'config.ini'
config.read(config_file)

TKN = config['DEFAULT']['TOKEN']
clogconfirm = config['CONFIRMS']['CLOGCONFIRM']

#bot setup
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='on.', intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
  bot.db = await aiosqlite.connect("data/pokemon.db")
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
  if message.author.id == 716390085896962058:
    if len(message.embeds) > 0:
      embed = message.embeds[0]
      if "appeared!" in embed.title and embed.image:
        url = embed.image.url
        await outnmodule(bot, message, url)

    elif 'The pokémon is ' in message.content:
      for i in hint_helper.solve(message.content):
        await hint_helper.hint_embed(i, message)

    elif 'Congratulations' in message.content and clogconfirm in 'Yy':
      await catch_helper.catch_identifier(bot, message)

  elif 'The pokémon is ' in message.content:
    for i in hint_helper.solve(message.content):
      await hint_helper.hint_embed(i, message)

bot.run(TKN)
