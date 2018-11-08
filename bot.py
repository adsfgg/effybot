#!/usr/bin/env python3
print("Starting discordbot...")

import logging,sys

use_console_logging = True

if len(sys.argv) == 2:
  if sys.argv[1] == "--no_console":
    use_console_logging = False

logging_level = logging.DEBUG

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
logger.info("Starting discordbot")

logger.info("Loading discord.py")
import discord
from discord.ext import commands
logger.info("Discord.py loaded ({0})".format(discord.__version__))
import traceback

with open("token.txt") as f:
  TOKEN = f.readlines()[0].replace("\n", "")

ASDF_ID = "134781032086896641"
BIG_BRAIN_ID = 421464243339001860
BOT_ERRORS_ID = 482931487767920640
PREFIX = "!"
pingbm = "What the fuck did you just @ me for, you little pinger? I’ll have you know I graduated top of my class in the @ spamming, and I’ve been involved in numerous secret raids on shitty minecraft servers, and I have over 300 confirmed @ pings. I am trained in @ warfare and I’m the top @ spammer in the entire @ spamming forces. You are nothing to me but just another person annoyed by the @ pings. I will @ you the fuck out with @ spam in the likes of which has never @'d before on this Earth, mark my fucking @ ping. You think you can get away with kick me over discord? Think again, fucker. As we speak I am activating secret network of bots and your server invite link is being traced right now so so you better prepare for about 100+ @ pings. The @ pings that wipes out the pathetic little thing you call your server. You’re fucking @'d, kiddo. I can @ you anywhere, anytime, and I can @ ping your server in over seven hundred ways, and that’s just with my bare keyboard. Not only am I extensively trained in CNTRL-C and CNTRL-V, but I have access to the entire arsenal of the entire Discord @ code and I will use it to its full extent to @ your miserable ass off the face of Discord, you little shit. If only you could have known what unholy @ pinging your little “clever” kick from the server was about to ping down upon you, maybe you would have held your fucking keyboard."

initial_extensions = []

logger.info("Loading initial_extensions...")

with open("initial_extensions.txt") as f:
  for line in f:
    initial_extensions.append(line[:-1]) #strip newline

logger.info("Loaded.")

from bot_commands import *

bot = commands.Bot(command_prefix=PREFIX)

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
  await channel.send(content=f"<@{ASDF_ID}>", embed=msg)
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
  if bot.user.mentioned_in(message) and message.content.startswith(f'<@{bot.user.id}>') and message.mention_everyone is False:
    #await message.channel.send(f'{message.author.mention}, my prefix is "{PREFIX}"')
                await message.channel.send(f'{message.author.mention} {pingbm}')
  elif cmd is not None:
    await process_bot_command(message, cmd, args)
  elif message.channel.id in ALLOWED_CHANNELS_ID:
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
    ctx = await bot.get_context(message)
    ctx.command = command
    ctx.args = args

    if command["has_args"]:
      argc = len(ctx.args)
      min_args = command["min_args"]
      max_args = command["max_args"]

      if argc < min_args:
        return await ctx.send("Not enough arguments. Needs at least {0} argument{1}".format(min_args, "s" if min_args > 1 else ""))
      elif argc > max_args:
        return await ctx.send("Too many arguments. Needs at most {0} argument{1}".format(max_args, "s" if max_args > 1 else ""))

      valid_args = command["valid_args"]

      for arg in args:
        if arg not in valid_args:
          return await ctx.send("Invalid argument \"{0}\". Must be one of {1}".format(arg,valid_args))

    on_command_func = ctx.command["on_command"]

    await on_command_func(ctx)

@bot.event
async def on_ready():
  logger.info("Logged in as {0.name} ({0.id})".format(bot.user))
  await bot.change_presence(activity=discord.Game(name="0w0 what's this"))

def main():
  logger.info("loading extensions")

  for extension in initial_extensions:
    try:
      bot.load_extension(extension)
      logger.info(f'Loaded extension {extension}.')

    except ModuleNotFoundError as e:
      logger.warning(f'Failed to load extension {extension}.')
      logger.debug(e)

  logger.info("Starting bot")

  bot.run(TOKEN)

if __name__ == "__main__":
  main()
