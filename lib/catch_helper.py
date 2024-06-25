import re
import configparser

from discord import Color, Embed

#config
config = configparser.ConfigParser()
config_file = 'config.ini'
config.read(config_file)

clog = int(config['DEFAULT']['CLOG'])

async def catch_identifier(bot, message):
  match = re.search(r' a level \d+ (\w+)!', message.content)
  pokeName = match.group(1).capitalize() if match else 'Unknown'
  await clog_embed(bot, pokeName, message)
  await message.channel.send(f"Catch sent to <#{clog}>!")


async def clog_embed(bot, pokeName, message):
  catlog = bot.get_channel(clog)
  embed = Embed(title='A New Pokemon Captured', color=Color.purple())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(name='Name', value=f'{pokeName}')
  embed.add_field(name='Captured Message', value=f'{message.content}')
  embed.add_field(name='Message Link',
                  value=f'[Jump to Message]({message.jump_url})')
  await catlog.send(embed=embed)

