from discord import Message, Embed
from discord.ext.commands import Cog, Bot
from utils import get_bible_queries, get_language_config_by_id
from connection import BibleRequest


class BibleCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message: Message):
        content = message.content
        queries = get_bible_queries(content)
        translation = get_language_config_by_id(message.guild.id)._translations

        for query in queries:
            book = query.split(" ")[0]

            try:
                book_name = translation[book]
                translation = get_language_config_by_id(message.guild.id)
                request = BibleRequest(book, query.split(" ")[1])
            except KeyError:
                translation = get_language_config_by_id(message.guild.id)
                await message.channel.send(embed=Embed(
                    description=translation.book_abbr_not_available + "\n" + translation.book_abbr_info + "\n[" + translation.abbreviation_url + "](" + translation.abbreviation_url + ")",
                    color=0xff0000))
