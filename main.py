import discord
from discord.ext import commands
import config
from fuzzywuzzy import process
import answers

data = config.load_config()

bot = commands.Bot(command_prefix=data.prefix, help_command=None, intents=discord.Intents.all())

@bot.event
async def on_message(message: discord.Message):
    channel = message.channel
    
    if message.author.bot:
        return    
    if data.channel_id != channel.id:
        return
    
    async with channel.typing():
        if process.extractOne(message.content, answers.greetings)[1] >= 80:
            await message.reply("И тебе привет <3", mention_author=False)
        else:
            await message.reply(message.content)

bot.run(data.token)
