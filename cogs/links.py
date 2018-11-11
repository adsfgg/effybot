import discord
from discord.ext import commands

class Links:

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def order(self, ctx):
    '''
    put glorious comrades in order
    '''

    await ctx.send("https://i.redd.it/x9triplll1v11.jpg")

  @commands.command()
  async def outplayed(self, ctx):
    '''
    would be russian div 1 champ
    '''

    await ctx.send("https://www.youtube.com/watch?v=MqQ5rKR3ddw&feature=youtu.be")

  @commands.command()
  async def kmac(self, ctx):
    '''
    ya wee numpty
    '''

    await ctx.send("https://cdn.discordapp.com/attachments/482716342244605952/494917661222764568/7k3l287nbqo11.png")
  
  @commands.command()
  async def star2(self, ctx):
    '''
    SOFT LOLI
    '''

    await ctx.send("https://www.youtube.com/watch?v=SGF_iTLdw4U")

  @commands.command()
  async def star(self, ctx):
    '''
    BUILD THE WALL
    '''
    
    await ctx.send("https://cdn.discordapp.com/attachments/463778061469351946/494876366861369354/JYgRGsOZNPUHLd6PEUUzL8WGULVESH4gd4kAfgjLXtM.png")

  @commands.command()
  async def brexit(self, ctx):
    '''
    STRONG AND STABLE
    '''
    await ctx.send("https://cdn.discordapp.com/attachments/421464243339001858/494543569340858368/q6att06f0fo11.png")  

  @commands.command()
  async def phone(self, ctx):
    '''
    phone on the fueld
    '''

    await ctx.send("https://cdn.discordapp.com/attachments/421464243339001858/489111874797830154/Capture.PNG")

  @commands.command()
  async def bigboy(self, ctx):
    '''
    Big Boii
    '''

    await ctx.send("https://clips.twitch.tv/BraveLongWrenTBCheesePull")
    
  @commands.command()
  async def kappa(self, ctx):
    '''
    Keepo
    '''

    await ctx.send("https://i.kym-cdn.com/photos/images/original/000/925/494/218.png_large")


def setup(bot):
  bot.add_cog(Links(bot))
