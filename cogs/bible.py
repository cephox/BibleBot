from discord import Message, Embed
from discord.ext.commands import Cog, AutoShardedBot
from utils import get_bible_queries, get_language_config_by_id, get_translation
from connection import BibleRequest
from datetime import datetime
from json.decoder import JSONDecodeError


class BibleCog(Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message: Message):
        content = message.content
        queries = get_bible_queries(content)

        for query in queries:
            translation = get_language_config_by_id(message.guild.id)._translations
            book = query.split(" ")[0]

            try:

                book_name = translation[book]
                translation = get_language_config_by_id(message.guild.id)
                try:
                    request = BibleRequest(book_name, query.split(" ")[1], get_translation(message.guild.id))
                except JSONDecodeError:
                    await message.channel.send(embed=Embed(
                        description=translation.quote_not_available,
                        color=0xff0000))
                    continue

                embed = Embed(title=request.book_name + " " + str(request.chapter))

                embed.set_footer(text="Bible quoted using getbible.net", icon_url=self.bot.user.avatar_url)
                embed.timestamp = datetime.utcnow()

                for verse in request.verses.keys():
                    embed.add_field(name=str(verse), value=request.verses[verse], inline=False)

                await message.channel.send(embed=embed)

            except KeyError:
                translation = get_language_config_by_id(message.guild.id)
                await message.channel.send(embed=Embed(
                    description=translation.book_abbr_not_available + "\n" + translation.book_abbr_info + "\n[" + translation.abbreviation_url + "](" + translation.abbreviation_url + ")",
                    color=0xff0000))
