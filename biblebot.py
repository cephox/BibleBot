from discord import Status, Activity, ActivityType, Embed
from discord.ext.commands import Bot, Context
from discord.ext.commands.errors import *
from config import Config
from utils import add_cogs, get_prefix_client, add_guild

from cogs.settings import SettingsCog

config = Config("config.json")

bot = Bot(command_prefix=get_prefix_client)


@bot.event
async def on_ready():
    await bot.change_presence(status=Status.online,
                              activity=Activity(type=ActivityType.watching, name="cool Bible Verses"))


@bot.event
async def on_guild_join(guild):
    await add_guild(guild)


@bot.event
async def on_guild_remove(guild):
    prefixes = config.prefix
    prefixes.pop(str(guild.id))
    config.save("prefix", prefixes)


@bot.event
async def on_command_error(ctx: Context, error):
    if isinstance(error, MissingPermissions):
        embed = Embed(description="You do not have the permission to execute this command")
        await ctx.send(embed=embed)


add_cogs(
    bot,
    SettingsCog
)

bot.run(config.token)
