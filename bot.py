#!/usr/bin/env python3
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename='/home/asdf/Dev/DiscordBot/log.txt', level=logging.INFO)
logging.info("starting discordbot")

import discord
from discord.ext import commands
import sys, traceback

with open("token.txt") as f:
	TOKEN = f.readlines()[0].replace("\n", "")

print(TOKEN)
ASDF_ID = "134781032086896641"
BIG_BRAIN_ID = 421464243339001860
BOT_ERRORS_ID = 482931487767920640
PREFIX = "!"

initial_extensions = ['cogs.test', 'cogs.basic', 'cogs.owner', 'cogs.games']

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CommandNotFound):
		return await ctx.send("Command not found. Try !help.")
	elif isinstance(error, commands.errors.MissingRequiredArgument):
		return await ctx.send(f"Missing required argument. Try !help {ctx.command.name}")
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
	logging.debug(error)

@bot.event
async def on_voice_state_update(member, before, after):
	if after.channel is not None and after.channel.id == BIG_BRAIN_ID:
		await add_big_text_role(member)
	else:
		await remove_big_text_role(member)

async def remove_big_text_role(user):
	logging.info(f"{user} left big brains, removing perms")

	role = discord.utils.get(user.guild.roles, name="big-text")

	logging.debug(role)

	await user.remove_roles(role)

async def add_big_text_role(user):
	logging.info(f"{user} joined big brains, adding perms")

	role = discord.utils.get(user.guild.roles, name="big-text")

	logging.debug(role)

	await user.add_roles(role)

@bot.event
async def on_ready():
	logging.info("Logged in as {0.name} ({0.id})".format(bot.user))
	await bot.change_presence(activity=discord.Game(name="0w0 what's this"))

def main():
	logging.info("loading extensions")

	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
			logging.info(f'Loaded extension {extension}.')
		except ModuleNotFoundError as e:
			logging.warning(f'Failed to load extension {extension}.')

	logging.info("starting bot")

	bot.run(TOKEN)

if __name__ == "__main__":
	main()
