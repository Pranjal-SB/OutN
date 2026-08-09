from discord import Color, Embed

from config import spawnlog
from constants import FOOTER

async def logthespawn(bot, message, name):
  splog = bot.get_channel(spawnlog)
  if splog is None:
    return
  embed = Embed(color=Color.green())
  embed.set_footer(text=FOOTER)
  embed.add_field(name='A pokemon spawned!', value=f'**__{name}__** spawned!')
  embed.add_field(name='Message Link', value=f'[Jump to Message]({message.jump_url})')
  await splog.send(embed=embed)
