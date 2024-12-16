import discord
from discord import app_commands
from selenium import webdriver
import time
from datetime import datetime
import asyncio

scheduled_tasks = {}

def fetch_chart():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    screenshot_path = "chart.png"
    try:
        chart_url = "http://127.0.0.1:8080"
        driver.get(chart_url)
        time.sleep(3)
        driver.save_screenshot(screenshot_path)
    finally:
        driver.quit()
    return screenshot_path

async def post_chart_loop(interval_seconds, channel):
    while True:
        try:
            screenshot_path = fetch_chart()
            current_time = datetime.now().strftime("%H:%M:%S | %d-%m-%Y")

            embed = discord.Embed(
                title="Chart Update",
                color=0x2F3136,
            )
            embed.set_image(url="attachment://chart.png")
            embed.set_footer(text=f"🕥 Generated at {current_time}")

            with open(screenshot_path, "rb") as file:
                await channel.send(file=discord.File(file, "chart.png"), embed=embed)

            await asyncio.sleep(interval_seconds)

        except asyncio.CancelledError:
            break
        except Exception as e:
            print(f"Error posting chart: {e}")
            await asyncio.sleep(interval_seconds)

async def lightweight_chart(tree: app_commands.CommandTree):
    @tree.command(name="chart", description="Setup the chart to post market updates at a specified interval.")
    @app_commands.describe(interval="Interval in seconds, minutes, or hours (e.g., 30s, 15min, 1h)",
                           channel="Target channel to send the chart updates")
    async def chart_command(interaction: discord.Interaction, interval: str, channel: discord.TextChannel):
        await interaction.response.send_message(f"Scheduling chart updates to {channel.mention}...", ephemeral=True)

        time_map = {"s": 1, "min": 60, "h": 3600}
        try:
            unit = "".join([char for char in interval if not char.isdigit()]).lower()
            value = int("".join([char for char in interval if char.isdigit()]))
            interval_seconds = value * time_map[unit]
        except (ValueError, KeyError):
            await interaction.followup.send("Invalid interval format. Use like '30s', '15min', or '1h'", ephemeral=True)
            return

        if channel.id in scheduled_tasks:
            scheduled_tasks[channel.id].cancel()

        task = asyncio.create_task(post_chart_loop(interval_seconds, channel))
        scheduled_tasks[channel.id] = task

        await interaction.followup.send(f"Chart updates will be posted every **{interval}** in {channel.mention}")
