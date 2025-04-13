import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import View, Button


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Zeigt das Hilfe-Menü mit Buttons", name="help")
    async def help(self, ctx):
        # Erstelle das Embed für das Hilfe-Menü
        embed = discord.Embed(
            title="Hilfe-Menü",
            description="Wähle eine der Optionen, um mehr zu erfahren.",
            color=discord.Color.purple()
        )
        embed.add_field(name="Allgemeine Infos", value="Erfahre mehr über den Bot.", inline=False)
        embed.add_field(name="⚙️ Configs", value="Siehe/Bearbeite die aktuellen Configs.", inline=False)

        # Erstelle die View mit Buttons
        view = HelpView()

        # Reagiere mit dem Embed und den Buttons
        await ctx.respond(embed=embed, view=view)


class HelpView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Allgemeine Infos", style=discord.ButtonStyle.primary, custom_id="help_general")
    async def general_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Allgemeine Infos",
            description="Hier findest du allgemeine Informationen zum Bot.\n\n"
                        "Dieser Bot bietet eine Vielzahl von Funktionen, darunter Benutzerinfos, "
                        "Server-Statistiken und vieles mehr.",
            color=discord.Color.green()
        )
        embed.add_field(name="Version", value="1.0.0", inline=False)
        embed.add_field(name="Ersteller", value="DeinName", inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="⚙️ Configs", style=discord.ButtonStyle.primary, custom_id="help_configs")
    async def configs_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Aktuelle Configs",
            description="Hier kannst du die aktuellen Konfigurationen des Bots einsehen und anpassen.\n\n"
                        "Verfügbare Befehle:\n"
                        "`/userinfo` - Zeigt Informationen über einen Benutzer\n"
                        "`/help` - Zeigt dieses Hilfe-Menü",
            color=discord.Color.blue()
        )
        await interaction.response.edit_message(embed=embed, view=self)


def setup(bot):
    bot.add_cog(Help(bot))
