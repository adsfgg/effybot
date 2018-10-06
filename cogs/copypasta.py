import discord
from discord.ext import commands

class CopyPasta:

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def daddy2(self, ctx):
		'''
		May God have mercy on our souls
		'''
		
		await ctx.send("Just me and my 💕daddy💕, hanging out I got pretty hungry🍆 so I started to pout 😞 He asked if I was down ⬇for something yummy 😍🍆 and I asked what and he said he'd give me his 💦cummies!💦 Yeah! Yeah!💕💦 I drink them!💦 I slurp them!💦 I swallow them whole💦 😍 It makes 💘daddy💘 😊happy😊 so it's my only goal... 💕💦😫Harder daddy! Harder daddy! 😫💦💕 1 cummy💦, 2 cummy💦💦, 3 cummy💦💦💦, 4💦💦💦💦 I'm 💘daddy's💘 👑princess 👑but I'm also a whore! 💟 He makes me feel squishy💗!He makes me feel good💜! 💘💘💘He makes me feel everything a little should!~ 💘💘💘 👑💦💘Wa-What!💘💦👑")

	@commands.command()
	async def springle(self, ctx):
		'''
		O OCEAN MAN
		'''

		await ctx.send("OCEAN MAN :ocean: :heart_eyes: Take me by the hand :raised_hand: lead me to the land that you understand :raised_hands: :ocean: OCEAN MAN :ocean: :heart_eyes: The voyage :bike: to the corner of the :earth_americas: globe is a real trip :ok_hand: :ocean: OCEAN MAN :ocean: :heart_eyes: The crust of a tan man :man_with_turban: imbibed by the sand :thumbsup: Soaking up the :sweat_drops: thirst of the land :100:")

def setup(bot):
	bot.add_cog(CopyPasta(bot))