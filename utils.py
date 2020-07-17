from discord.ext.commands import Cog
from config import config
import re
from translations import Translations
import json


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
        config.reload()
        languages = config.language
        return languages[str(id)]


def get_language_config(language):
    return Translations(language)


def get_language_config_by_id(id):
    return Translations(get_language(id))


def get_default_bible_translation(id):
    return Translations(get_language(id)).default_translation


def get_translation(id):
    translations = config.translation
    try:
        return translations[str(id)]
    except KeyError:
        add_guild_by_id(id)
        config.reload()
        translations = config.translation
        return translations[str(id)]


def get_possible_translations(id):
    return Translations(get_language(id)).bible_translations


async def get_prefix_client(client, message):
    prefixes = config.prefix
    try:
        return prefixes[str(message.guild.id)], f"<@!{client.user.id}> ", f"<@{client.user.id}> "
    except KeyError:
        add_guild(message.guild)
        config.reload()
        prefixes = config.prefix
        return prefixes[str(message.guild.id)], f"<@!{client.user.id}> ", f"<@{client.user.id}> "


async def get_prefix(message):
    prefixes = config.prefix
    try:
        return prefixes[str(message.guild.id)]
    except KeyError:
        add_guild(message.guild)
        config.reload()
        return prefixes[str(message.guild.id)]


def add_guild(guild):
    add_guild_by_id(guild.id)


def add_guild_by_id(id):
    # prefixes = config.prefix
    # translations = config.language
    # languages = config.translation
    # languages[str(id)] = "en"
    # prefixes[str(id)] = "."
    # translations[str(id)] = get_default_bible_translation(str(id))
    # config.save("prefix", prefixes)
    # config.save("language", languages)
    # config.save("translation", translations)

    data = json.load(open("config.json"))
    data["prefix"][str(id)] = "."
    data["language"][str(id)] = "en"
    data["translation"][str(id)] = "kjv"
    json.dump(data, open("config.json", "w"), indent=4)
