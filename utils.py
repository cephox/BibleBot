from discord.ext.commands import Cog
from config import Config


def add_cogs(bot, *cogs):
    for cog_c in cogs:
        if cog_c is None:
            continue
        cog: Cog = cog_c(bot)
        bot.add_cog(cog)


async def get_prefix_client(client, message):
    config = Config("config.json")
    prefixes = config.prefix
    try:
        return prefixes[str(message.guild.id)], f"<@!{client.user.id}> ", f"<@{client.user.id}> "
    except KeyError:
        await add_guild(message.guild)
        return prefixes[str(message.guild.id)], f"<@!{client.user.id}> ", f"<@{client.user.id}> "


async def get_prefix(client, message):
    config = Config("config.json")
    prefixes = config.prefix
    try:
        return prefixes[str(message.guild.id)]
    except KeyError:
        await add_guild(message.guild)
        return prefixes[str(message.guild.id)]


async def add_guild(guild):
    config = Config("config.json")
    prefixes = config.prefix
    prefixes[str(guild.id)] = "."
    config.save("prefix", prefixes)
