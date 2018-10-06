import discord
from discord.ext import commands
import logging

class PictureLists:

	thinking_lines = []
	springu_lines = []
	
	def __init__(self, bot):
		self.bot = bot
		self.logger = logging.getLogger('Discord_Bot.PictureLists')

		self.logger.info("Loading thinking_lines...")

		with open("res/thinking_lines.txt") as f:
			for line in f:
				self.thinking_lines.append(line)

		self.logger.info("Loaded thinking_lines")
		self.logger.info("Loading springu_lines...")

		with open("res/springu_lines.txt") as f:
			for line in f:
				self.springu_lines.append(line)

		self.logger.info("Loaded springu_lines.")
			
	@commands.command()
	async def springu(self, ctx, *, index : int = None):
		'''
		breadstick
		'''

		length = len(self.springu_lines) - 1
		
		if index == None:
			num = random.randint(0, length)
		else:
			num = index

		if num > length or num < 0:
			return await ctx.send("Index must be between 0 and {0}".format(length))

		msg = self.springu_lines[num]
		
		await ctx.send(msg)

	@commands.command()
	async def bigspringu(self, ctx):
		'''
		really big breadstick
		'''

		for i in range(big_springu_limit):
			num = random.randint(0, len(self.springu_lines) - 1)

			msg = self.springu_lines[num]
			await ctx.send(msg)

	@commands.command(hidden=True)
	@commands.is_owner()
	async def bigspringulimit(self, ctx, *, limit : int):
		if limit <= 0:
			msg = discord.Embed(title="Set Limit", description=limit, color=0x00FF00)
			msg.add_field(name="Status", value=":x:Error", inline=False)
			msg.add_field(name="Error", value="Limit cannot be less than 0", inline=False)
			await ctx.send(embed=msg)

		try:
			global big_springu_limit
			big_springu_limit = limit
		except Exception as e:
			msg = discord.Embed(title="Set Limit", description=limit, color=0x00FF00)
			msg.add_field(name="Status", value=":x:Error", inline=False)
			msg.add_field(name="Error", value=e, inline=False)
			await ctx.send(embed=msg)
		else:
			msg = discord.Embed(title="Set Limit", description=limit, color=0x00FF00)
			msg.add_field(name="Status", value=":white_check_mark:Success", inline=False)
			await ctx.send(embed=msg)

	@commands.command()
	async def think(self, ctx, *, index : int = None):
		'''
		Big think
		'''

		length = len(self.thinking_lines) - 1
		
		if index == None:
			num = random.randint(0, length)
		else:
			num = index

		if num > length or num < 0:
			return await ctx.send("Index must be between 0 and {0}".format(length))

		msg = self.thinking_lines[num]
		
		await ctx.send(msg)

	@commands.command()
	async def bigthink(self, ctx):
		'''
		Really big think
		'''

		for i in range(big_think_limit):
			num = random.randint(0, len(self.thinking_lines) - 1)

			msg = self.thinking_lines[num]
			await ctx.send(msg)

	@commands.command(hidden=True)
	@commands.is_owner()
	async def bigthinklimit(self, ctx, *, limit : int):
		if limit <= 0:
			msg = discord.Embed(title="Set Limit", description=limit, color=0x00FF00)
			msg.add_field(name="Status", value=":x:Error", inline=False)
			msg.add_field(name="Error", value="Limit cannot be less than 0", inline=False)
			await ctx.send(embed=msg)

		try:
			global big_think_limit
			global think_timeout_limit
			big_think_limit = limit
		except Exception as e:
			msg = discord.Embed(title="Set Limit", description=limit, color=0x00FF00)
			msg.add_field(name="Status", value=":x:Error", inline=False)
			msg.add_field(name="Error", value=e, inline=False)
			await ctx.send(embed=msg)
		else:
			msg = discord.Embed(title="Set Limit", description=limit, color=0x00FF00)
			msg.add_field(name="Status", value=":white_check_mark:Success", inline=False)
			await ctx.send(embed=msg)

def setup(bot):
	bot.add_cog(PictureLists(bot))