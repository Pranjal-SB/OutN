"""Startup validation for the IDs in config.ini.

Every configured ID is resolved once at login. A wrong ID, or a channel the bot
cannot see, used to surface only as a spawn that quietly never got starred.
"""

import discord

import config

# (label, id, kind) — kind is 'channel' or 'role'
def _entries():
  return [
      ('rare ping', config.rping if config.rpingconfirm else None, 'role'),
      ('regional ping', config.regping if config.regpingconfirm else None, 'role'),
      ('starboard', config.starch if config.starchconfirm else None, 'channel'),
      ('catch log', config.clog if config.clogconfirm else None, 'channel'),
      ('spawn log', config.spawnlog if config.spawnlogconfirm else None, 'channel'),
  ]


def _resolve_role(bot, role_id):
  for guild in bot.guilds:
    role = guild.get_role(role_id)
    if role is not None:
      return f"@{role.name} ({guild.name})"
  return None


def _resolve_channel(bot, channel_id):
  channel = bot.get_channel(channel_id)
  if channel is None:
    return None
  guild = getattr(channel, 'guild', None)
  return f"#{channel.name}" + (f" ({guild.name})" if guild else "")


def check(bot):
  """Print a per-setting report. Returns the number of broken settings."""
  print(f"\n{'Config check':^40}")
  print('-' * 40)

  broken = 0
  for label, value, kind in _entries():
    if value is None:
      print(f"  {label:<14} off")
      continue

    found = (_resolve_role(bot, value) if kind == 'role'
             else _resolve_channel(bot, value))
    if found:
      print(f"  {label:<14} {found}")
    else:
      broken += 1
      print(f"  {label:<14} {value}  <-- NOT FOUND")

  if broken:
    print(f"\n  {broken} setting(s) point at an ID this bot cannot see.")
    print("  Check the ID is right and that the bot was invited to that server.")
    print("  Delete config.ini to run setup again.")
  print('-' * 40)
  return broken


async def check_permissions(bot):
  """Warn about missing permissions in the channels the bot writes to."""
  needed = {'send_messages': 'Send Messages',
            'embed_links': 'Embed Links',
            'add_reactions': 'Add Reactions'}

  for label, value, kind in _entries():
    if value is None or kind != 'channel':
      continue
    channel = bot.get_channel(value)
    if channel is None or not isinstance(channel, discord.TextChannel):
      continue
    perms = channel.permissions_for(channel.guild.me)
    missing = [name for attr, name in needed.items() if not getattr(perms, attr)]
    if missing:
      print(f"  {label}: missing {', '.join(missing)} in #{channel.name}")
