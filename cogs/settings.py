from discord import Embed
from discord.ext.commands import Cog, Bot, group, Context, guild_only, has_permissions
from utils import get_prefix
from config import Config


class SettingsCog(Cog):
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
            embed = Embed(title="Bible Bot Settings for " + ctx.guild.name,
                          description=f"Please use `{await get_prefix(self.bot, ctx.message)}settings <setting>` for more Information",
                          color=0x34bdeb)
            embed.add_field(name="Prefix Settings",
                            value=f"Current Prefix: `{await get_prefix(self.bot, ctx.message)}`\n"
                                  f"Type `{await get_prefix(self.bot, ctx.message)}settings prefix <new Prefix>` to change the Prefix")

            await ctx.send(embed=embed)

    @settings.command(name="prefix")
    @has_permissions(administrator=True)
    @guild_only()
    async def prefix(self, ctx: Context, *args):
        if args:
            config = Config("config.json")
            prefixes = config.prefix
            prefixes[str(ctx.guild.id)] = args[0]
            config.save("prefix", prefixes)

            await ctx.send(embed=Embed(description=f"Prefix changed to `{await get_prefix(self.bot, ctx.message)}`", color=0x34bdeb))
            return
        await ctx.send(embed=Embed(title="Prefix for " + ctx.guild.name,
                                   description=f"Your current Prefix: `{await get_prefix(self.bot, ctx.message)}`\n"
                                               f"Change by typing `{await get_prefix(self.bot, ctx.message)}settings prefix <new Prefix>`", color=0x34bdeb))
