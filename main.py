import sys
import discord
from discord.ext import commands

sys.path.append('lib')
from config import get_config, TKN, clogconfirm
from TheOutNModule import outnmodule, identifycmd
import hint_helper
import catch_helper
import cmd_embeds

version = 'v8'

#config
get_config()

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

  elif 'on.' in message.content:
    msg = message.content
    chnl = message.channel

    if 'help' in msg.lower():
      await cmd_embeds.help_embed(chnl)

    elif 'identify' in msg.lower():
      if message.attachments:
        url = message.attachments[0].url
        await identifycmd(message, url)


bot.run(TKN)
