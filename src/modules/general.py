import discord, random
from discord.ext import commands

PHONE_ID = "150009549196099584"
KMAC_ID = "206283655159480320"
BOOWER_ID = "152526530239660034"
NIGHTS_ID = "153153882355138560"
ASDF_ID = "134781032086896641"
big_think_limit = 3
big_springu_limit = 3

class General:

  thinking_lines = []
  springu_lines = []

  def __init__(self, bot):
    self.bot = bot

  @commands.command(hidden=True)
  async def bigbrains(self, ctx):
    '''
    the brain chamber
    '''
    
    await ctx.send("BIG BRAINS ONLY <@{0}> <@{1}> <@{2}> <@{3}>".format(KMAC_ID, BOOWER_ID, ASDF_ID, PHONE_ID))

  @commands.command()
  async def emo(self, ctx):
    '''
    im dead inside
    '''

    await ctx.send("I'm so baaadddd <@{0}> :sob:".format(ASDF_ID))

  @commands.command()
  async def jjonak(self, ctx):
    '''
    Is there anyone who can stop this man
    '''

    await ctx.send("LITERAL WALKING BRAIN <@{0}>".format(KMAC_ID));

  @commands.command()
  async def hello(self, ctx):
    '''
    Say hello!
    '''

    msg = 'Hello {0.author.mention}!'.format(ctx.message)
    await ctx.send(msg)


  @commands.command(aliases=["regard"])
  async def thank(self, ctx, *, name:str = None):
    '''
    Thank the bot for its unpayed work
    '''

    msg = ":ok_hand: {0.mention}"

    if name == None:
      msg=msg.format(ctx.message.author)
    else:
      users = ctx.bot.get_all_members()
      match = None

      for user in users:
        if user.name.lower() == name.lower():
          match = user
          break
        elif not user.nick == None:
          if user.nick.lower() == name.lower():
            match = user
            break

      if match == None:
        msg = f"Couldn't thank \"{name}\" because I couldn't find them :sob:"
      else:
        msg=msg.format(match)

    await ctx.send(msg)

  @commands.command()
  async def look(self, ctx):
    '''
    Give them the looker
    '''

    await ctx.send(":eyes:")

  @commands.command()
  async def ping(self, ctx):
    '''
    Ping pong!
    '''

    await ctx.send("Pong! {0}".format(ctx.message.author.mention))

  @commands.command()
  async def daddy(self, ctx):
    '''
    DADDY NO
    '''

    await ctx.send("<@{0}> DADDY NO".format(PHONE_ID))

def setup(bot):
  bot.add_cog(General(bot))
