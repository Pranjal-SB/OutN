import logging
import sys

import aiohttp
import discord

sys.path.append('lib')
from config import TKN, clogconfirm
from constants import POKETWO_ID, PREFIX, VERSION
from TheOutNModule import outnmodule, identifycmd
import config_check
import hint_helper
import catch_helper
import cmd_embeds

# File handler so an overnight crash leaves something to read.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
    handlers=[
        logging.FileHandler('outn.log', encoding='utf8'),
        logging.StreamHandler(),
    ],
)

# message_content is the only privileged intent the bot needs; nothing here
# reads member data, so the members intent stays off.
intents = discord.Intents.default()
intents.message_content = True


class OutNClient(discord.Client):
  """discord.Client, not commands.Bot: every command here is dispatched by hand
  in on_message, and process_commands was never called, so the command
  framework was dead weight."""

  async def setup_hook(self):
    # One session for the bot's lifetime. Per-request sessions meant a fresh
    # TCP + TLS handshake on every single spawn.
    self.http_session = aiohttp.ClientSession()

  async def close(self):
    await self.http_session.close()
    await super().close()


bot = OutNClient(intents=intents)


@bot.event
async def on_ready():
  print(f"{'='*40}")
  print(f"{'The OutN Project':^40}")
  print(f"{'='*40}")
  print(f"{'Version:':<10} {VERSION}")
  print(f"{'GitHub:':<10} {'https://github.com/Pranjal-SB/OutN'}")
  print()
  print(f"{'Logged in as':<10} {bot.user.name}#{bot.user.discriminator}")
  print(f"{'Bot User ID:':<10} {bot.user.id}")
  print(f"{'='*40}")

  config_check.check(bot)
  await config_check.check_permissions(bot)

  await bot.change_presence(status=discord.Status.online, activity=discord.Game("Pokémon"))


async def solve_hints(message):
  await hint_helper.hint_embed(hint_helper.solve(message.content), message)


async def handle_command(message):
  # startswith, not `in`: 'check python.on.that help' used to fire the help embed.
  command = message.content[len(PREFIX):].strip().lower()

  if command.startswith('help'):
    await cmd_embeds.help_embed(message.channel)

  elif command.startswith('identify'):
    if not message.attachments:
      # Used to do nothing at all, which reads as the bot being broken.
      await message.channel.send(
          f"Attach an image to the message, like `{PREFIX}identify` + the spawn picture.")
      return
    await identifycmd(bot, message, message.attachments[0].url)


@bot.event
async def on_message(message):
  if message.author.id == POKETWO_ID:
    if message.embeds:
      embed = message.embeds[0]
      if embed.title and "appeared!" in embed.title and embed.image:
        await outnmodule(bot, message, embed.image.url)

    elif hint_helper.HINT_PREFIX in message.content:
      await solve_hints(message)

    elif 'Congratulations' in message.content and clogconfirm:
      await catch_helper.catch_identifier(bot, message)

  elif message.author.bot:
    return

  elif hint_helper.HINT_PREFIX in message.content:
    await solve_hints(message)

  elif message.content.startswith(PREFIX):
    await handle_command(message)


bot.run(TKN)
