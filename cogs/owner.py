import subprocess, sys, discord
from discord.ext import commands
import logging

class Owner:

	initial_extensions = []
	logger = None

	def __init__(self, bot):
		self.bot = bot
		self.logger = logging.getLogger('Discord_Bot.Owner')
	
	@commands.command(name='load')
	@commands.is_owner()
	async def cog_load(self, ctx, *, cog: str):
		'''
		Loads the given module
		'''

		self.logger.info(f"Loading cog: {cog}")

		try:
			self.bot.load_extension(cog)
		except Exception as e:
			self.logger.info(f"Failed to load cog: {cog}")
			self.logger.debug(e)

			msg = discord.Embed(title="Load Extension", description=cog, color=0xFF0000)
			msg.add_field(name="Status", value=":x: Error", inline=False)
			msg.add_field(name="Error", value=e, inline=False)
			await ctx.send(embed=msg)
		else:
			self.logger.info(f"Loaded cog {cog}")

			msg = discord.Embed(title="Load Extension", description=cog, color=0x00FF00)
			msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
			await ctx.send(embed=msg)

	@commands.command(name='unload')
	@commands.is_owner()
	async def cog_unload(self, ctx, *, cog: str):
		'''
		Unloads the given module
		'''

		self.logger.info(f"Unloading cog: {cog}")

		try:
			self.bot.unload_extension(cog)
		except Exception as e:
			self.logger.info(f"Failed to unload cog: {cog}")
			self.logger.debug(e)

			msg = discord.Embed(title="Unload Extension", description=cog, color=0xFF0000)
			msg.add_field(name="Status", value=":x: Error", inline=False)
			msg.add_field(name="Error", value=e, inline=False)
			await ctx.send(embed=msg)
		else:
			self.logger.info(f"Unloaded cog: {cog}")

			msg = discord.Embed(title="Unload Extension", description=cog, color=0x00FF00)
			msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
			await ctx.send(embed=msg)

	@commands.command(name='reload')
	@commands.is_owner()
	async def cog_reload(self, ctx, *, cog: str):
		'''
		Reloads the given module
		'''

		self.logger.info(f"Reloading cog: {cog}")

		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
		except Exception as e:
			self.logger.info(f"Failed to reload cog: {cog}")
			self.logger.debug(e)

			msg = discord.Embed(title="Reload Extension", description=cog, color=0xFF0000)
			msg.add_field(name="Status", value=":x: Error", inline=False)
			msg.add_field(name="Error", value=e, inline=False)
			await ctx.send(embed=msg)
		else:
			self.logger.info(f"Successfuly reloaded cog: {cog}")
			msg = discord.Embed(title="Reload Extension", description=cog, color=0x00FF00)
			msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
			await ctx.send(embed=msg)

	@commands.command()
	@commands.is_owner()
	async def reset(self, ctx):
		'''
		Soft resets the bot
		'''
		
		self.logger.info("Resetting the bot...")
		for extension in self.initial_extensions:
			try:
				self.bot.unload_extension(extension)
				self.bot.load_extension(extension)
				self.logger.info(f'Loaded extension {extension}.')
			except ModuleNotFoundError as e:
				self.logger.warning(f'Failed to load extension {extension}.')
				msg = discord.Embed(title="Failed to load extension", description=extension, color=0xFF0000)

		msg = discord.Embed(title="Reset", color=0x00FF00)
		msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
		await ctx.send(embed=msg)
		self.logger.info("Bot reset.")

	@commands.command()
	@commands.is_owner()
	async def latency(self, ctx):
		'''
		Gets the latency of the bot. 
		'''

		msg = self.bot.latency 

		await ctx.send(msg)

	async def _shutdown_bot(self):
		try:
			aiosession.close()
		except:
			pass
		await self.bot.logout()

	@commands.command()
	@commands.is_owner()
	async def restart(self, ctx):
		'''
		Restarts the bot
		'''

		self.logger.info("Restarting bot...")
		await ctx.send("Restarting...")
		await self._shutdown_bot()

def setup(bot):
	bot.add_cog(Owner(bot))
