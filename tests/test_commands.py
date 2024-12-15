import unittest
from unittest.mock import AsyncMock
import discord
from discord import app_commands
from commands.test import test

class TestCommands(unittest.IsolatedAsyncioTestCase):
    async def test_command(self):
        client = discord.Client(intents=discord.Intents.default())
        tree = app_commands.CommandTree(client)

        interaction = AsyncMock(spec=discord.Interaction)
        
        interaction.response = AsyncMock()
        interaction.response.send_message = AsyncMock()

        await test(tree)
        test_cmd = tree.get_command("test")

        await test_cmd.callback(interaction)

        interaction.response.send_message.assert_awaited_once_with("I'm working")

if __name__ == "__main__":
    unittest.main()
    