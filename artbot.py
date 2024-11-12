import discord
from discord.ext import commands
import settings
from dotenv import load_dotenv
import random
import classes

logger = settings.logging.getLogger("bot")


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
    discord_token = settings.DISCORD_TOKEN

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user}, ID: {bot.user.id}")

    @bot.command(
            aliases=["p"],
            help="this is help",
            description="this is discription",
            brief="this is brief"
    )
    async def ping(ctx):
        """Answers with pong"""
        await ctx.send("pong")
    
    @bot.command()
    async def say(ctx, *user_input):
        if user_input:
            await ctx.send(" ".join(user_input))
        else:
            await ctx.send("WHAT!")
    
    @bot.command()
    async def dice(ctx, *options):
        await ctx.send(random.choice(options))

    @bot.command()
    async def joined(ctx, who : discord.Member):
        await ctx.send(who.joined_at)

    @bot.command()
    async def slap(ctx, reason : classes.Slapper(use_nicknames=True)):
        await ctx.send(reason)

    bot.run(discord_token, root_logger=True)


