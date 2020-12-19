import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='\\?')

@bot.command()
async def Jobs(ctx):
	await ctx.send("Commands: \n\n1. '.me'\n2. '.xp'")

class main(discord.Client):
	async def on_reading(self):
		print("", self.user)

	async def on_messages(self, message):
		if message.author != self.user: 
			print("Hey, I don't understand")

		# don't send this code 	
		if	message.author == self.user:
			return

		if message.content == ".help":
			await message.channel.send("Hi!")

client = main()
client.run('token')