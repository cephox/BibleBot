from discord import Embed
from discord.ext.commands import Cog, Bot, group, Context, guild_only, has_permissions
from utils import get_prefix, get_language_config_by_id
from config import config


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
            settings = get_language_config_by_id(ctx.guild.id)
            embed = Embed(title=settings.f_general_settings_embed_title(ctx.guild.name),
                          description=settings.f_general_settings_embed_description(await get_prefix(ctx.message)),
                          color=0x34bdeb)

            embed.add_field(name=settings.general_settings_embed_field_prefix_title,
                            value=settings.f_general_settings_embed_field_prefix_description(
                                await get_prefix(ctx.message), await get_prefix(ctx.message)))

            await ctx.send(embed=embed)

    @settings.command(name="prefix")
    @has_permissions(administrator=True)
    @guild_only()
    async def prefix(self, ctx: Context, *args):
        settings = get_language_config_by_id(ctx.guild.id)

        if args:
            print(1)
            prefixes = config.prefix
            prefixes[str(ctx.guild.id)] = args[0]
            config.save("prefix", prefixes)
            print(2)

            await ctx.send(
                embed=Embed(description=settings.f_prefix_successfully_changed(await get_prefix(ctx.message)), color=0x34bdeb))
            print(3)
            return
        await ctx.send(embed=Embed(title=settings.f_prefix_settings_embed_title(ctx.guild.name),
                                   description=settings.f_prefix_settings_embed_description(await get_prefix(ctx.message), await get_prefix(ctx.message)),
                                   color=0x34bdeb))
