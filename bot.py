import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='P')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(725784168755232808)
    await channel.send(f'{member} 痛苦的開始!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(725780030701174794)
    await channel.send(f'{member} 因承受不了壓力而死去了!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')


bot.run('NzI1NzYzMTk3OTQ4MTMzNDM2.XvT4NA.Tf2rLuLcQuwUAqKv0hKuTKIxIbQ')