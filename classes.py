import discord
from discord.ext import commands
import random
import settings

class Slapper(commands.Converter):
    use_nicknames: bool

    def __init__(self, *, use_nicknames):
        self.use_nicknames = use_nicknames

    async def convert(self, ctx, argument="fish"):
        someone = random.choice(ctx.guild.members)
        name = ctx.author
        if self.use_nicknames:
            name = name.nick
        return f"{ctx.author} slapped {someone} with {argument}"
