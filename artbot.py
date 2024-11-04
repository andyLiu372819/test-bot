import discord
from discord.ext import commands
import os
import settings
from dotenv import load_dotenv

load_dotenv()


def handle_user_input(msg):
    message = msg.lower()
    if message == "hi":
        return "hi there"
    else:
        return "hello user, welcome"


async def processMessage(msg, u_msg):
    try:
        feedback = handle_user_input(u_msg)
        await msg.channel.send(feedback)
    except Exception as error:
        print (error)

def runBot():
    intent = discord.Intents.all()
    bot = commands.Bot(command_prefix="/", intents=intent)
    discord_token = os.getenv("DISCORD_TOKEN")
    client = discord.Client(intents=discord.Intents.default())

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("_________________")

    @client.event
    async def on_ready():
        print((client.user), 'is live')

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return 
        await processMessage(msg, 'hi')

    bot.run(discord_token)


