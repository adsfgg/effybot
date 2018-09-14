import subprocess, sys, discord
from discord.ext import commands

class Owner:
	def __init__(self, bot):
		self.bot = bot
		self.debug = False
	
	# Hidden means it won't show up on the default help.
	@commands.command(name='load', hidden=True)
	@commands.is_owner()
	async def cog_load(self, ctx, *, cog: str):
		"""Command which Loads a Module.
		Remember to use dot path. e.g: cogs.owner"""

		try:
			self.bot.load_extension(cog)
		except Exception as e:
			msg = discord.Embed(title="Load Extension", description=cog, color=0xFF0000)
			msg.add_field(name="Status", value=":x: Error", inline=False)
			msg.add_field(name="Error", value=e, inline=False)
			await ctx.send(embed=msg)
		else:
			msg = discord.Embed(title="Load Extension", description=cog, color=0x00FF00)
			msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
			await ctx.send(embed=msg)

	@commands.command(name='unload', hidden=True)
	@commands.is_owner()
	async def cog_unload(self, ctx, *, cog: str):
		"""Command which Unloads a Module.
		Remember to use dot path. e.g: cogs.owner"""

		try:
			self.bot.unload_extension(cog)
		except Exception as e:
			msg = discord.Embed(title="Unload Extension", description=cog, color=0xFF0000)
			msg.add_field(name="Status", value=":x: Error", inline=False)
			msg.add_field(name="Error", value=e, inline=False)
			await ctx.send(embed=msg)
			# await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
		else:
			msg = discord.Embed(title="Unload Extension", description=cog, color=0x00FF00)
			msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
			await ctx.send(embed=msg)
			# await ctx.send('**`SUCCESS`**')

	@commands.command(name='reload', hidden=True)
	@commands.is_owner()
	async def cog_reload(self, ctx, *, cog: str):
		"""Command which Reloads a Module.
		Remember to use dot path. e.g: cogs.owner"""

		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
		except Exception as e:
			msg = discord.Embed(title="Reload Extension", description=cog, color=0xFF0000)
			msg.add_field(name="Status", value=":x: Error", inline=False)
			msg.add_field(name="Error", value=e, inline=False)
			await ctx.send(embed=msg)
			# await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
		else:
			msg = discord.Embed(title="Reload Extension", description=cog, color=0x00FF00)
			msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
			await ctx.send(embed=msg)
			# await ctx.send('**`SUCCESS`**')

	@commands.command(hidden=True)
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

	@commands.command(hidden=True)
	@commands.is_owner()
	async def restart(self, ctx):
		"""Restarts the bot"""
		await ctx.send("Restarting...")
		await self._shutdown_bot()

def setup(bot):
	bot.add_cog(Owner(bot))
