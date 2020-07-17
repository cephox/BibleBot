from discord import Embed
from discord.ext.commands import Cog, Bot, group, Context, guild_only, has_permissions
from utils import get_prefix, get_language_config_by_id, get_language, get_translation, get_possible_translations, get_default_bible_translation
from config import config
import os
import yaml


class SettingsCog(Cog, name="Settings"):
    def __init__(self, bot: Bot):
        self.bot = bot

    @group(name="settings", aliases=["config"])
    @has_permissions(administrator=True)
    @guild_only()
    async def settings(self, ctx: Context):
        """
        Manage the Settings of BibleBot
        """
        if ctx.invoked_subcommand is None:
            message = await ctx.send(embed=Embed(description="Gathering Information ..."))

            settings = get_language_config_by_id(ctx.guild.id)

            embed = Embed(title=settings.f_general_settings_embed_title(ctx.guild.name),
                          description=settings.f_general_settings_embed_description(await get_prefix(ctx.message)),
                          color=0x34bdeb)

            embed.add_field(name=settings.general_settings_embed_field_prefix_title,
                            value=settings.f_general_settings_embed_field_prefix_description(
                                await get_prefix(ctx.message), await get_prefix(ctx.message)))

            embed.add_field(name=settings.general_settings_embed_field_language_title,
                            value=settings.f_general_settings_embed_field_language_description(
                                get_language(ctx.guild.id), await get_prefix(ctx.message)))

            embed.add_field(name=settings.general_settings_embed_field_translation_title,
                            value=settings.f_general_settings_embed_field_translation_description(
                                get_translation(ctx.guild.id), await get_prefix(ctx.message)))

            await message.edit(embed=embed)

    @settings.command(name="translation")
    @has_permissions(administrator=True)
    @guild_only()
    async def translation(self, ctx: Context, *args):
        language_config = get_language_config_by_id(ctx.guild.id)

        if args and args[0] in get_possible_translations(ctx.guild.id):

            translation = config.translation
            translation[str(ctx.guild.id)] = args[0]
            config.save("translation", translation)

            await ctx.send(
                embed=Embed(
                    description=language_config.f_translation_successfully_changed(get_translation(ctx.guild.id)),
                    color=0x34bdeb))

            return

        print(1)
        embed = Embed(title=language_config.f_translation_settings_embed_title(ctx.guild.name),
                      description=language_config.f_translation_settings_embed_description(
                          get_translation(ctx.guild.id), await get_prefix(ctx.message)),
                      color=0x34bdeb)

        embed.add_field(name=language_config.supported_translations,
                        value="\n".join([f"`{i}`" for i in get_possible_translations(ctx.guild.id)]))

        await ctx.send(embed=embed)

    @settings.command(name="language")
    @has_permissions(administrator=True)
    @guild_only()
    async def language(self, ctx: Context, *args):
        settings = get_language_config_by_id(ctx.guild.id)

        if args:
            langs = config.language
            translation = config.translation
            langs[str(ctx.guild.id)] = args[0]
            config.save("language", langs)

            translation[str(ctx.guild.id)] = get_default_bible_translation(str(ctx.guild.id))
            config.save("translation", translation)

            settings = get_language_config_by_id(ctx.guild.id)

            await ctx.send(
                embed=Embed(description=settings.f_language_successfully_changed(get_language(ctx.guild.id)),
                            color=0x34bdeb))

            return

        embed = Embed(title=settings.f_language_settings_embed_title(ctx.guild.name),
                      description=settings.f_language_settings_embed_description(
                          get_language(ctx.guild.id), await get_prefix(ctx.message)),
                      color=0x34bdeb)

        langs = dict()

        for filename in os.listdir("./translations"):
            if filename.endswith(".yml"):
                yaml_file = yaml.safe_load(open(f"translations/{filename}"))
                langs[filename[:-4]] = yaml_file["language-name"]

        description = ""
        for l in langs.keys():
            description += f"`{l}` | " + langs[l] + "\n"

        embed.add_field(name=settings.supported_languages, value=description, inline=False)
        await ctx.send(embed=embed)

    @settings.command(name="prefix")
    @has_permissions(administrator=True)
    @guild_only()
    async def prefix(self, ctx: Context, *args):
        settings = get_language_config_by_id(ctx.guild.id)

        if args:
            prefixes = config.prefix
            prefixes[str(ctx.guild.id)] = args[0]
            config.save("prefix", prefixes)

            await ctx.send(
                embed=Embed(description=settings.f_prefix_successfully_changed(await get_prefix(ctx.message)),
                            color=0x34bdeb))

            return
        await ctx.send(embed=Embed(title=settings.f_prefix_settings_embed_title(ctx.guild.name),
                                   description=settings.f_prefix_settings_embed_description(
                                       await get_prefix(ctx.message), await get_prefix(ctx.message)),
                                   color=0x34bdeb))
