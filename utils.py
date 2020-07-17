from discord.ext.commands import Cog
from config import config
import re
from translations import Translations


def get_bible_queries(message: str):
    m = re.findall("\\[\\w+ \\d+:\\d+[0-9,-]+\\]", message)
    return [i.replace("[", "").replace("]", "") for i in m]


def add_cogs(bot, *cogs):
    for cog_c in cogs:
        if cog_c is None:
            continue
        cog: Cog = cog_c(bot)
        bot.add_cog(cog)


def get_language(id):
    languages = config.language
    try:
        return languages[str(id)]
    except KeyError:
        add_guild_by_id(id)
        languages = config.language
        return languages[str(id)]


def get_language_config(language):
    return Translations(language)


def get_language_config_by_id(id):
    return Translations(get_language(id))


async def get_prefix_client(client, message):
    prefixes = config.prefix
    try:
        return prefixes[str(message.guild.id)], f"<@!{client.user.id}> ", f"<@{client.user.id}> "
    except KeyError:
        add_guild(message.guild)
        prefixes = config.prefix
        return prefixes[str(message.guild.id)], f"<@!{client.user.id}> ", f"<@{client.user.id}> "


async def get_prefix(message):
    prefixes = config.prefix
    try:
        return prefixes[str(message.guild.id)]
    except KeyError:
        add_guild(message.guild)
        return prefixes[str(message.guild.id)]


def add_guild(guild):
    add_guild_by_id(guild.id)


def add_guild_by_id(id):
    prefixes = config.prefix
    languages = config.language
    languages[str(id)] = "en"
    prefixes[str(id)] = "."
    config.save("prefix", prefixes)
    config.save("language", languages)
