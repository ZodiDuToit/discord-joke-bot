
import requests
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

url = "https://icanhazdadjoke.com/search"

@client.event
async def on_message(message):
	
	if message.author != client.user:

		response = requests.get(url, headers={"Accept": "application/json"},params={"term":message.content})

		try:
			await message.channel.send(response.json()["results"][2]["joke"])

		except:
			await message.channel.send("no such topic")

client.run("your token here")
