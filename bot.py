import discord
import logging
from discord.ext import commands

# .env
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True 

bot = commands.Bot(command_prefix="!", intents=intents)

# events
@bot.event
async def on_ready():
    logging.info(f"logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Template!"))

for folder in os.listdir("./cogs"):
    try:
        bot.load_extension(f"cogs.{folder}.__init__")
        logging.info(f"Cog {folder} loaded!")
    except Exception as e:
        logging.error(f"Cog {folder} not loaded, error: {e}")


bot.run(os.getenv("token"))