import discord
import os
from dotenv import load_dotenv
from commands.setup import setup_bot

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await setup_bot(client)

client.run(DISCORD_TOKEN)
