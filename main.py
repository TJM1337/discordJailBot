import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import time
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.presences = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "hai pa" in message.content.lower():
        await message.channel.send("hai pa")
    
    await bot.process_commands(message)


@bot.command()
async def jail(ctx, member: discord.Member, seconds: int):
    jail_channel = discord.utils.get(ctx.guild.voice_channels, name="PUSCARIE")

    await ctx.send(f"o7 {member} for {seconds}s")

    for i in range(seconds):
        await member.move_to(jail_channel)
        await asyncio.sleep(1)

    await bot.process_commands(ctx)


@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said {msg}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)