import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Kicke einen User!")
    @commands.has_role("Dev")
    async def kick(
        self,
        ctx,
        member: Option(discord.Member, "Wähle den User"),
        grund: Option(str, "Gib den Grund für den Kick ein")
    ):
        try:
            await member.kick(reason=grund)
        except discord.Forbidden:
            await ctx.respond("```Ich habe keine Berechtigung, um diesen User zu kicken!```")
            return
        await ctx.respond(f"{member.mention} wurde gekickt.\n**Grund:** {grund}")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.respond("```Du hast keine Berechtigung, diesen Befehl zu verwenden!```", ephemeral=True)
        else:
            await ctx.respond(f"Es ist ein Fehler aufgetreten: ```{error}```", ephemeral=True)
            raise error  # Optional: nur zum Debuggen

def setup(bot):
    bot.add_cog(Kick(bot))
