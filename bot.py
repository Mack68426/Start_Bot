import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(">> Bot is Online <<")


bot.run('MTAwMDQ0NDU1MDI4NTg5Nzg3MA.GB6K-n.2dllGh2swv_TqzV59zTBq-rcQ0u1q7rIu2dErI')

