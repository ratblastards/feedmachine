import nextcord
from nextcord.ext import commands, tasks

import os

BOT_TOKEN = os.getenv('FEEDMACHINE_TOKEN')
SELF_USER = os.getenv('FEEDMACHINE_USERID')
OUTPUT_FILE = "data/status.txt"

# SELF_USER = 116661373043212292

intents = nextcord.Intents.default()

intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix=':', intents=intents)
last_game = "(startup)"

@bot.event
async def on_ready():
	print('Bot is ready.')

@bot.event
async def on_presence_update(before, after):

	global last_game

	if after.bot:
		return

	if after.id != SELF_USER:
		return

	game = "offline"
	for a in after.activities:
		if a.__class__.__name__ == "Game":
			if a.type == nextcord.ActivityType.playing:
				game = a.name

	if game != last_game:
		print("Activity:", game)
		with open(OUTPUT_FILE, "w") as outfile:
			outfile.write(game)
		last_game = game

bot.run(BOT_TOKEN)
