import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class Announcement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Lass den Bot eine wichtige Ankündigung senden")
    async def announce(
            self,
            ctx,
            text: Option(str, "Die Ankündigung, die du machen möchtest"),
            channel: Option(discord.TextChannel, "Der Kanal, in dem die Ankündigung gesendet werden soll"),
            title: Option(str, "Optionaler Titel der Ankündigung"),
    ):
        # Optionaler Titel der Ankündigung
        announcement = f"**{title}**\n\n{text}"

        # Sende die Ankündigung als normalen Text
        await channel.send(announcement)

        # Bestätige dem User, dass die Ankündigung gesendet wurde
        await ctx.respond("Die Ankündigung wurde gesendet!", ephemeral=True)


def setup(bot):
    bot.add_cog(Announcement(bot))
