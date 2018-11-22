import subprocess, sys, discord
from discord.ext import commands
import logging, json

class Owner:
  
  def __init__(self, bot):
    self.bot = bot
    self.logger = logging.getLogger('Discord_Bot.Owner')

    self.logger.info("Loading modules...")
    
    with open("configs/settings.json") as f:
      settings = json.load(f)
    
    self.modules = settings["modules"]

    self.logger.info("Loaded.")

  @commands.command(name='load')
  @commands.is_owner()
  async def module_load(self, ctx, *, module: str):
    '''
    Loads the given module
    '''

    self.logger.info(f"Loading module: {module}")

    try:
      self.bot.load_extension("modules." + module)
    except Exception as e:
      self.logger.warning(f"Failed to load module: {module}")
      self.logger.debug(e)

      msg = discord.Embed(title="Load Module", description=module, color=0xFF0000)
      msg.add_field(name="Status", value=":x: Error", inline=False)
      msg.add_field(name="Error", value=e, inline=False)
      await ctx.send(embed=msg)
    else:
      self.logger.info(f"Loaded Module {module}")

      msg = discord.Embed(title="Load Module", description=module, color=0x00FF00)
      msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
      await ctx.send(embed=msg)

  @commands.command(name='unload')
  @commands.is_owner()
  async def module_unload(self, ctx, *, module: str):
    '''
    Unloads the given module
    '''

    self.logger.info(f"Unloading module: {module}")

    try:
      self.bot.unload_extension("modules." + module)
    except Exception as e:
      self.logger.info(f"Failed to unload module: {module}")
      self.logger.debug(e)

      msg = discord.Embed(title="Unload Module", description=module, color=0xFF0000)
      msg.add_field(name="Status", value=":x: Error", inline=False)
      msg.add_field(name="Error", value=e, inline=False)
      await ctx.send(embed=msg)
    else:
      self.logger.info(f"Unloaded module: {module}")

      msg = discord.Embed(title="Unload Module", description=module, color=0x00FF00)
      msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
      await ctx.send(embed=msg)

  @commands.command(name='reload')
  @commands.is_owner()
  async def module_reload(self, ctx, *, module: str):
    '''
    Reloads the given module
    '''

    self.logger.info(f"Reloading module: {module}")

    try:
      self.bot.unload_extension("modules." + module)
      self.bot.load_extension("modules." + module)
    except Exception as e:
      self.logger.warning(f"Failed to reload module: {module}")
      self.logger.debug(e)

      msg = discord.Embed(title="Reload Module", description=module, color=0xFF0000)
      msg.add_field(name="Status", value=":x: Error", inline=False)
      msg.add_field(name="Error", value=e, inline=False)
      await ctx.send(embed=msg)
    else:
      self.logger.info(f"Successfuly reloaded module: {module}")
      msg = discord.Embed(title="Reload Module", description=module, color=0x00FF00)
      msg.add_field(name="Status", value=":white_check_mark: Success", inline=False)
      await ctx.send(embed=msg)

  @commands.command()
  @commands.is_owner()
  async def reset(self, ctx):
    '''
    Soft resets the bot
    '''
    
    self.logger.info("Resetting the bot...")
    unloaded = 0
    loaded = 0
    
    for module in self.modules:
      try:
        self.bot.unload_extension(module["filepath"])
        unloaded = unloaded + 1
        if module["enabled"]:
          self.bot.load_extension(module["filepath"])
          loaded = loaded + 1
          self.logger.info(f'Loaded module {module["name"]}.')
      except ModuleNotFoundError as e:
        self.logger.warning(f'Failed to load module {module["name"]}.')
        msg = discord.Embed(title="Failed to load module", description=module, color=0xFF0000)

    msg = discord.Embed(title="Reset", description=f"Reset {len(self.modules)} modules", color=0x00FF00)
    msg.add_field(name="Modules", value=f"Unloaded: {unloaded}, Loaded: {loaded}", inline=False)
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
