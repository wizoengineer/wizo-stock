import discord
from discord import app_commands

async def test(tree: app_commands.CommandTree):
    @tree.command(name="test", description="See if bot responds")
    async def test(interaction: discord.Interaction):
        await interaction.response.send_message("I'm working")
