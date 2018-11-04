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

	@commands.command()
	async def kashtts(self, ctx):
		'''
		Out with the old, in with the new I say.
		'''

		await ctx.send(":alarm_clock::alarm_clock: Just because kash writes:writing_hand:️ a lot of questionable :grey_question: :grey_question: dumb shit :poop: doesn't mean :smirk::smirk::smirk: HE is :u6709: DUMB 🧐🧐. He is :u6709: not a dumb guy :boy::boy: he simply chooses to repeatedly write :writing_hand: dumb stuff :pouch: over a wide time :watch: span. Kash is :u6709: a smart 🧠🧠 person :bust_in_silhouette::bust_in_silhouette::bust_in_silhouette: he just makes bad :chart_with_downwards_trend::chart_with_downwards_trend: decisions Jesus :cross:️ why :thinking: do you all pick :pick::pick: on :on::on: him you bullies:left_fist::skin-tone-1: :right_fist::skin-tone-1:", tts=True)

def setup(bot):
	bot.add_cog(TTS(bot))
