import discord
from discord import app_commands
import importlib
import inspect
import commands

async def load_commands(tree: app_commands.CommandTree):
    for module_name in commands.__all__:
        module = importlib.import_module(f"commands.{module_name}")

        for name, func in inspect.getmembers(module, predicate=inspect.iscoroutinefunction):
            if "tree" in inspect.signature(func).parameters:
                print(f"Registering command: {name}")
                await func(tree)

    print("Commands ✅")

async def setup_bot(client: discord.Client):
    tree = app_commands.CommandTree(client)
    await load_commands(tree)
    await tree.sync()
    print("Bot ✅")
