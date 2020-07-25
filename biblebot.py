from discord import Status, Activity, ActivityType, Embed
from discord.ext.commands import AutoShardedBot, Context
from discord.ext.commands.errors import MissingPermissions
from config import config
from utils import add_cogs, get_prefix_client, add_guild, get_language_config_by_id, send_help

from cogs.settings import SettingsCog
from cogs.bible import BibleCog

bot = AutoShardedBot(command_prefix=get_prefix_client)
bot.remove_command("help")


@bot.command(aliases=["?"])
async def help(ctx: Context):
    await send_help(ctx)


@bot.event
async def on_ready():
    await bot.change_presence(status=Status.online,
                              activity=Activity(type=ActivityType.watching, name="cool Bible Verses"))


@bot.event
async def on_guild_join(guild):
    add_guild(guild)


@bot.event
async def on_guild_remove(guild):
    prefixes = config.prefix
    translations = config.translation
    languages = config.language
    prefixes.pop(str(guild.id))
    translations.pop(str(guild.id))
    languages.pop(str(guild.id))
    config.save("prefix", prefixes)
    config.save("translation", translations)
    config.save("language", languages)
    config.reload()


@bot.event
async def on_command_error(ctx: Context, error):
    if isinstance(error, MissingPermissions):
        embed = Embed(description=get_language_config_by_id(ctx.guild.id).missing_permission_error_message,
                      color=0xff0000)
        await ctx.send(embed=embed)


add_cogs(
    bot,
    BibleCog,
    SettingsCog
)

bot.run(config.token)
