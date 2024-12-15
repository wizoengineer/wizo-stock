import discord
from discord import app_commands
import importlib
import commands

async def load_commands(tree: app_commands.CommandTree):
    for module_name in commands.__all__:
        module = importlib.import_module(f"commands.{module_name}")
        await module.setup(tree)
    print("Commands ✅")

async def setup_bot(client: discord.Client):
    tree = app_commands.CommandTree(client)
    await load_commands(tree)
    await tree.sync()
    print("Bot ✅")
