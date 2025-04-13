import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from datetime import datetime
import pytz


class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Zeigt Informationen über einen User", name="userinfo", aliases=["info"])
    async def userinfo(
            self,
            ctx,
            user: Option(discord.Member, "Gib einen User an", default=None)
    ):
        if user is None:
            user = ctx.author

        embed1 = discord.Embed(
            title=f"Infos über {user.name}",
            description=f"Hier siehst du alle Infos über {user.mention}",
            color=discord.Color.purple()
        )

        time1 = discord.utils.format_dt(user.created_at, "R")
        time2 = discord.utils.format_dt(user.created_at, "f")

        embed1.add_field(name="Account erstellt:", value=time1)

        # Format the creation date with European date format
        european_date_format = "%d-%m-%Y %H:%M:%S"
        time2_european = datetime.strftime(user.created_at, european_date_format)

        embed1.add_field(name="Erstell Datum:", value=time2_european)
        embed1.add_field(name="ID", value=user.id, inline=False)

        embed1.set_thumbnail(url=user.display_avatar.url)

        german_time_zone = pytz.timezone("Europe/Berlin")

        # Format the current time in European date format for the footer
        current_time_format = "%d-%m-%Y %H:%M:%S"
        current_time = datetime.now(german_time_zone).strftime(current_time_format)

        embed1.set_footer(text=f"{current_time}")

        await ctx.respond(embed=embed1)


def setup(bot):
    bot.add_cog(Userinfo(bot))
