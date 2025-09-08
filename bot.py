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
    
bot.load_extension("cogs.judges-mention-cog.__init__")
bot.load_extension("cogs.judges-appeals-cog.__init__")
# to load cog use this for example: bot.load_extension("cogs.judges-mention-cog.__init__")
bot.run(os.getenv("token"))