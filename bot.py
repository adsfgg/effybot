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

import discord
from discord.ext import commands
import traceback

with open("token.txt") as f:
	TOKEN = f.readlines()[0].replace("\n", "")

ASDF_ID = "134781032086896641"
BIG_BRAIN_ID = 421464243339001860
BOT_ERRORS_ID = 482931487767920640
BOT_CENTRAL_ID = 446243019205640212
PREFIX = "!"

initial_extensions = []

logger.info("Loading initial_extensions...")

with open("initial_extensions.txt") as f:
	for line in f:
		initial_extensions.append(line[:-1]) #strip newline

logger.info("Loaded.")

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
	logger.info(f"{user} left big brains, removing perms")
	
	channel = discord.utils.get(user.guild.channels, name="big-text")

	await channel.set_permissions(user, read_messages=False)

async def add_to_text(user):
	logger.info(f"{user} joined big brains, adding perms")

	channel = discord.utils.get(user.guild.channels, name="big-text")	

	await channel.set_permissions(user, read_messages=True)

@bot.event
async def on_message(message):
	if message.author.bot: return
	if bot.user.mentioned_in(message) and message.mention_everyone is False:
		await message.channel.send(f'{message.author.mention}, my prefix is "{PREFIX}"')
	elif message.channel.id == BOT_CENTRAL_ID:
		await bot.process_commands(message)

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
