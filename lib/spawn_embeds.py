from discord import Embed

from config import rpingconfirm, regpingconfirm, rping, regping
from constants import COLOR_COMMON, FOOTER


async def spawn_embed(message, name, phrase=None, color=COLOR_COMMON, ping=None):
  """Announce a spawn.

  `phrase` is the tier blurb, e.g. 'A mythic Pokemon spawned!'. None means a
  plain common spawn. `ping` is a role ID to ping after the embed, or None.
  """
  value = (f'**__{name}__**, {phrase} catch it using:' if phrase
           else f'**__{name}__** spawned! catch it using:')

  embed = Embed(color=color)
  embed.set_footer(text=FOOTER)
  embed.add_field(name='New Spawn!', value=value)
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)

  if ping is not None:
    await message.channel.send(f"<@&{ping}>")


def rare_ping():
  return rping if rpingconfirm else None


def regional_ping():
  return regping if regpingconfirm else None
