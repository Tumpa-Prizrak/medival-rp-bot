import discord
from discord.ext import commands
import config

data = config.load_config()

bot = commands.Bot(command_prefix=data.prefix, help_command=None, intents=discord.Intents.all())

@bot.event
async def on_message(message: discord.Message):
    pass

bot.run(data.token)
