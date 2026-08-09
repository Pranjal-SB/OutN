from discord import Color, Embed

from config import clog
from constants import FOOTER

async def catch_identifier(bot, message):
  if await clog_embed(bot, message):
    await message.channel.send(f"Catch sent to <#{clog}>!")


async def clog_embed(bot, message):
  catlog = bot.get_channel(clog)
  if catlog is None:
    return False
  embed = Embed(title='A New Pokemon Captured', color=Color.purple())
  embed.set_footer(text=FOOTER)
  embed.add_field(name='Captured Message', value=f'{message.content}')
  embed.add_field(name='Message Link',
                  value=f'[Jump to Message]({message.jump_url})')
  await catlog.send(embed=embed)
  return True

