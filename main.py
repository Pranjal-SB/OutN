import configparser
import sys
import keep_alive
import os

import discord
from discord.ext import commands

sys.path.append('lib')
from TheOutNModule import outnmodule
import hint_helper
import catch_helper

version = 'v7.1'

TKN = os.environ['token']
clogconfirm = os.environ['clogconfirm']

#bot setup
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='on.', intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
  print(f"{'='*40}")
  print(f"{'The OutN Project':^40}")
  print(f"{'='*40}")
  print(f"{'Version:':<10} {version}")
  print(f"{'GitHub:':<10} {'https://github.com/Pranjal-SB/OutN'}")
  print()
  print(f"{'Logged in as':<10} {bot.user.name}#{bot.user.discriminator}")
  print(f"{'Bot User ID:':<10} {bot.user.id}")
  print(f"{'='*40}")
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

keep_alive.keep_alive()
bot.run(TKN)
