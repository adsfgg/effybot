import discord, random
from discord.ext import commands

class Games:

	ball_answers = []

	def __init__(self, bot):
		self.bot = bot

		ball_file = open("res/8ball_answers.txt")

		for line in ball_file:
			self.ball_answers.append(line)

		ball_file.close()
		
	@commands.command(pass_context=True, name="8ball")
	async def eightball(self, ctx, *, question:str):
		'''
		You can use 8ball to answer a question.
		'''
	 
		num = random.randint(0, len(self.ball_answers) - 1)

		answer = self.ball_answers[num]

		msg = discord.Embed(description=str(ctx.message.author), color=0x00FF00)
		msg.add_field(name=":question: Question", value=question, inline=False)
		msg.add_field(name=":8ball: Answer", value=answer, inline=False)

		await ctx.send(embed=msg)

	@commands.command(aliases=["coin", "toss"], pass_context=True)
	async def flip(self, ctx):
		'''
		Flip a coin.
		'''

		num = random.randint(0,1)
		if num == 1:
			msg = "Heads!"
		else:
			msg = "Tails!"
		await ctx.send(msg)

def setup(bot):
	bot.add_cog(Games(bot))
