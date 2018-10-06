import discord
from discord.ext import commands

class TTS:

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def bauerthink(self, ctx):
		'''
		BauerThinkins🤔
		'''

		await ctx.send("bauerthinkins bauerthinkins bauerthinkins bauerthinkins", tts=True)

	@commands.command()
	async def cab(self, ctx):
		'''
		Spam the noodle to help cabooble
		'''

		await ctx.send("What :question: the hell :japanese_goblin: cab :taxi: I'm over here :point_down: making hilarious :rofl: , deep :thinking: , and politically correct :gay_pride_flag: jokes and these guys :person_with_blond_hair::skin-tone-5: do low effort shit :poop: posts and you laugh :rofl: the hardest :eggplant: I've ever seen :eyes: . I don't get it, cab :question: :question: :question:", tts=True)

	@commands.command()
	async def bauer(self, ctx):
		'''
		bauerJONKINS
		'''

		await ctx.send("bauerjankins bauerjankins bauerjankins bauerjankins bauerjankins bauerjankins", tts=True)
	

def setup(bot):
	bot.add_cog(TTS(bot))
