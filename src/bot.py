#!/usr/bin/env python3
print("Starting discordbot...")

import discord
from discord.ext import commands
import logging,sys,json

from custom_commands import *

# bot setup

use_console_logging = True
logging_level = logging.DEBUG
BIG_BRAIN_ID = 421464243339001860

if len(sys.argv) == 2 and sys.argv[1] == "--no-console":
  use_console_logging = False

logger = logging.getLogger("Discord_Bot")
logger.setLevel(logging_level)

#log file
fh = logging.FileHandler("log.txt")
fh.setLevel(logging_level)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#console log
if use_console_logging:
  ch = logging.StreamHandler()
  ch.setLevel(logging_level)
  ch.setFormatter(formatter)
  logger.addHandler(ch)

fh.setFormatter(formatter)

logger.addHandler(fh)

logger.info("Logging setup successfully")

logger.info("Using Discord.py ({0})".format(discord.__version__))

logger.info("Loading credentials...")

creds = []
with open("configs/bot.json") as f:
  creds = json.load(f)

bot_name = creds["name"]
TOKEN = creds["token"]
OWNER_ID = creds["owner_id"]

logger.info("Loaded credentials")

logger.info("Loading settings...")

settings = []
with open("configs/settings.json") as f:
  settings = json.load(f)

PREFIX = settings["prefix"]
BOT_ERRORS_ID = settings["bot_errors_channel_id"]
ping_response = settings["ping_response"]
set_allowed_channels(settings["allowed_channels"])
modules = settings["modules"]

logger.info("Loaded settings")

bot = commands.Bot(command_prefix=PREFIX)

# bot event handling

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CommandNotFound):
    return await ctx.send(f"Command not found. Try {PREFIX}help.")
  elif isinstance(error, commands.errors.MissingRequiredArgument):
    return await ctx.send(f"Missing required argument. Try {PREFIX}help {ctx.command.name}")
  elif isinstance(error, commands.errors.BadArgument):
    return await ctx.send(f"Bad argument. Try {PREFIX}help {ctx.command.name}")
  elif isinstance(error, commands.errors.NotOwner):
    msg = discord.Embed(title=":x:", description="You do not have permission to run this command.", color=0xFF0000)
    return await ctx.send(embed=msg)
  elif isinstance(error, commands.DisabledCommand):
    return await ctx.send("That command is currently disabled. Please try again later.")

  await ctx.send("I had an error :sob: Please try again later.")
  channel = bot.get_channel(BOT_ERRORS_ID)
  msg = discord.Embed(title="Command Error", description=str(type(error)), color=0xFF0000)
  msg.add_field(name="Command", value=ctx.message.content, inline=False)
  msg.add_field(name="Error", value=error, inline=False)
  await channel.send(content=f"<@{OWNER_ID}>", embed=msg)
  logger.debug(error)

@bot.event
async def on_voice_state_update(member, before, after):
  if after.channel is not None and after.channel.id == BIG_BRAIN_ID and (before.channel is None or not before.channel.id == BIG_BRAIN_ID):
    await add_to_text(member)
  elif after.channel is None or not after.channel.id == BIG_BRAIN_ID:
    await remove_from_text(member)

async def remove_from_text(user):
  channel = discord.utils.get(user.guild.channels, name="big-text")

  await channel.set_permissions(user, read_messages=False)

async def add_to_text(user):
  channel = discord.utils.get(user.guild.channels, name="big-text") 

  await channel.set_permissions(user, read_messages=True)

@bot.event
async def on_message(message):
  cmd, args = get_command(message)

  if message.author.bot: return
  if bot.user.mentioned_in(message) and (message.content.startswith(f'<@{bot.user.id}>') or message.content.startswith(f'<@!{bot.user.id}>')) and message.mention_everyone is False:
    await message.channel.send(f'{message.author.mention} {ping_response}')
  elif cmd is not None:
    await process_bot_command(message, cmd, args)
  elif message.channel.id in get_allowed_channels():
    await bot.process_commands(message)

def get_command(message):
  for cmd in bot_commands:
    cmd_name = f"{PREFIX}{cmd['name']}"
    if message.content.startswith(f"{cmd_name} ") or message.content == f"{cmd_name}":
      args = message.content.split(" ")[1:]

      return cmd, args

  return None, None

async def process_bot_command(message, command, args):
  if command is not None:
    if command["owner_only"]:
      if message.author.id != OWNER_ID:
        msg = discord.Embed(title=":x:", description="You do not have permission to run this command.", color=0xFF0000)
        return await message.channel.send(embed=msg)
    ctx = await bot.get_context(message)
    ctx.command = command
    ctx.args = args

    if command["has_args"]:
      argc = len(ctx.args)
      
      try:
        num_args = command["num_args"]
        if argc != num_args:
          return await ctx.send("Incorrect number of arguments. Needs {0} argument{1}".format(num_args, "s" if num_args > 1 else ""))
      except KeyError as e:
        try:
          min_args = command["min_args"]
          max_args = command["max_args"]

          if argc < min_args:
            return await ctx.send("Not enough arguments. Needs at least {0} argument{1}".format(min_args, "s" if min_args > 1 else ""))
          elif argc > max_args:
            return await ctx.send("Too many arguments. Needs at most {0} argument{1}".format(max_args, "s" if max_args > 1 else ""))
        except KeyError as e:
          return logger.error("Command \"{0}\" not defined correctly. has_args is true, but no arg limit is defined.".format(command["name"]))

      valid_args = command["valid_args"]

      for arg in args:
        if arg not in valid_args:
          return await ctx.send("Invalid argument \"{0}\". Must be one of {1}".format(arg,valid_args))

    on_command_func = ctx.command["on_command"]

    await on_command_func(ctx)

@bot.event
async def on_ready():
  logger.info("Logged in as {0.name} ({0.id})".format(bot.user))
  presence = settings["presence"]
  if presence != "":
    await bot.change_presence(activity=discord.Game(name=presence))
    logger.info("Changing presence to: " + presence)

def main():
  logger.info("Loading initial modules")
  
  for module in modules:
    try:
      if module["enabled"]:
        bot.load_extension(module["filepath"])
        logger.info(f'Loaded module {module["name"]}.')
      else:
        logger.info(f'Skipping loading module: {module["name"]}')
    except ModuleNotFoundError as e:
      logger.warning(f'Failed to load module {module["name"]}.')
      logger.debug(e)

  logger.info("Starting bot")
  bot.run(TOKEN)

if __name__ == "__main__":
  main()
