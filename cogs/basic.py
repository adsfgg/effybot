import discord, random
from discord.ext import commands

PHONE_ID = "150009549196099584"
KMAC_ID = "206283655159480320"
NIGHTS_ID = "153153882355138560"
ASDF_ID = "134781032086896641"
big_think_limit = 3
big_springu_limit = 3

class Basic:

	thinking_lines = []
	springu_lines = []

	def __init__(self, bot):
		self.bot = bot

		with open("res/thinking_lines.txt") as f:
			for line in f:
				self.thinking_lines.append(line)

		with open("res/springu_lines.txt") as f:
			for line in f:
				self.springu_lines.append(line)

	@commands.command(hidden=True)
	async def kmac(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/482716342244605952/494917661222764568/7k3l287nbqo11.png")
	
	@commands.command(hidden=True)
	async def bauerthink(self, ctx):
		await ctx.send("bauerthinkins bauerthinkins bauerthinkins bauerthinkins", tts=True)

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
	async def daddy2(self, ctx):
		'''
		May god have mercy on our souls
		'''
		
		await ctx.send("Just me and my 💕daddy💕, hanging out I got pretty hungry🍆 so I started to pout 😞 He asked if I was down ⬇for something yummy 😍🍆 and I asked what and he said he'd give me his 💦cummies!💦 Yeah! Yeah!💕💦 I drink them!💦 I slurp them!💦 I swallow them whole💦 😍 It makes 💘daddy💘 😊happy😊 so it's my only goal... 💕💦😫Harder daddy! Harder daddy! 😫💦💕 1 cummy💦, 2 cummy💦💦, 3 cummy💦💦💦, 4💦💦💦💦 I'm 💘daddy's💘 👑princess 👑but I'm also a whore! 💟 He makes me feel squishy💗!He makes me feel good💜! 💘💘💘He makes me feel everything a little should!~ 💘💘💘 👑💦💘Wa-What!💘💦👑")

	@commands.command(hidden=True)
	async def cab(self, ctx):
		await ctx.send("What :question: the hell :japanese_goblin: cab :taxi: I'm over here :point_down: making hilarious :rofl: , deep :thinking: , and politically correct :gay_pride_flag: jokes and these guys :person_with_blond_hair::skin-tone-5: do low effort shit :poop: posts and you laugh :rofl: the hardest :eggplant: I've ever seen :eyes: . I don't get it, cab :question: :question: :question:", tts=True)

	@commands.command(hidden=True)
	async def bauer(self, ctx):
		await ctx.send("bauerjankins bauerjankins bauerjankins bauerjankins bauerjankins bauerjankins", tts=True)
	
	@commands.command(hidden=True)
	async def phone(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/421464243339001858/489111874797830154/Capture.PNG")

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
		
	@commands.command()
	async def springle(self, ctx):
		'''
		O OCEAN MAN
		'''

		await ctx.send("OCEAN MAN :ocean: :heart_eyes: Take me by the hand :raised_hand: lead me to the land that you understand :raised_hands: :ocean: OCEAN MAN :ocean: :heart_eyes: The voyage :bike: to the corner of the :earth_americas: globe is a real trip :ok_hand: :ocean: OCEAN MAN :ocean: :heart_eyes: The crust of a tan man :man_with_turban: imbibed by the sand :thumbsup: Soaking up the :sweat_drops: thirst of the land :100:")

	@commands.command()
	async def springu(self, ctx, *, index : int = None):
		'''
		SPAM THIS NOODLE TO HELP SPRINGDOOLE
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

	@commands.command(hidden=True)
	async def bigspringu(self, ctx):	
		for i in range(big_springu_limit):
			num = random.randint(0, len(self.springu_lines) - 1)

			msg = self.springu_lines[num]
			await ctx.send(msg)

	@commands.command()
	async def days(self, ctx):
		'''
		summon der König 😊
		'''

		await ctx.send("It's day and <@{0}>!".format(NIGHTS_ID))

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

	@commands.command(hidden=True)
	async def bigboy(self, ctx):
		'''
		Big Boii
		'''
		await ctx.send("https://clips.twitch.tv/BraveLongWrenTBCheesePull")

	@commands.command(enabled=False, hidden=True)
	async def bigboyvoice(self, ctx):
		'''
		A big boii joins the voice
		'''
		await ctx.send("oops not added yet :wink:")

	@commands.command()
	async def kappa(self, ctx):
		'''
		Keepo
		'''
		await ctx.send("https://i.kym-cdn.com/photos/images/original/000/925/494/218.png_large")

	@commands.command()
	async def hello(self, ctx):
		'''
		Say hello!
		'''

		msg = 'Hello {0.author.mention}!'.format(ctx.message)
		await ctx.send(msg)

	@commands.command()
	async def think(self, ctx, *, index : int = None):
		'''
		Really big think
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
		Really really big think
		'''

		for i in range(big_think_limit):
			num = random.randint(0, len(self.thinking_lines) - 1)

			msg = self.thinking_lines[num]
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

	@commands.command(hidden=True)
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

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
	bot.add_cog(Basic(bot))
