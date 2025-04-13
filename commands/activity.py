import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Ändere den Status beliebig")
    @commands.has_role("Dev")
    async def activity(
            self, ctx,
            typ: Option(str, choices=["game", "stream"]),
            name: Option(str)
    ):
        try:
            if typ == "game":
                act = discord.Game(name=name)
            else:
                act = discord.Streaming(
                    name=name,
                    url="https://www.twitch.tv/bastighg"
                )

            await self.bot.change_presence(activity=act, status=discord.Status.online)
            await ctx.respond("Aktivität wurde geändert!", ephemeral=True)

        except discord.Forbidden:
            await ctx.respond("```Ich habe keine Berechtigung, die Aktivität zu ändern!```", ephemeral=True)
        except Exception as error:
            await ctx.respond(f"Es ist ein Fehler aufgetreten: ```{error}```", ephemeral=True)

    @slash_command(description="Setze die Aktivität zurück")
    async def online(self, ctx):
        try:
            total_members = sum(guild.member_count for guild in self.bot.guilds)
            game = discord.Game(name=f"with {total_members} users")
            await self.bot.change_presence(activity=game)
            await ctx.respond("Aktivität wurde zurückgesetzt!", ephemeral=True)

        except discord.Forbidden:
            await ctx.respond("```Ich habe keine Berechtigung, den Status zurückzusetzen!```", ephemeral=True)
        except Exception as error:
            await ctx.respond(f"Es ist ein Fehler aufgetreten: ```{error}```", ephemeral=True)

def setup(bot):
    bot.add_cog(Activity(bot))
