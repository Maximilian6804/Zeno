import os

import discord
from discord.commands import Option
from dotenv import load_dotenv




intents = discord.Intents.default()

intents.members = True
intents.message_content = True

bot = discord.Bot(
    intents=intents,
    debug_guilds=[1155564626050826394]
)

@bot.event
async def on_ready():
    print(f"{bot.user} ist nun Hochgefahren!")


@bot.slash_command(description="Lass den Bot eine wichtige Ankündigung senden")
async def announce(
        ctx,
        text: Option(str, "Die Ankündigung, die du machen möchtest"),
        channel: Option(discord.TextChannel)
):
    await channel.send(text)
    await ctx.respond("Die Ankündigung wurde gesendet", ephemeral=True)



#automatischer cog loader
if __name__ == "__main__":
    for category in ['commands', 'tasks', 'listener']:
        if os.path.exists(f'./{category}'):  # Prüft, ob der Ordner existiert
            for filename in os.listdir(f'./{category}'):
                if filename.endswith('.py'):
                    bot.load_extension(f'{category}.{filename[:-3]}')


load_dotenv()

token = os.getenv("TOKEN")
if not token:
    print("Fehler: TOKEN wurde nicht geladen. Überprüfe deine .env-Datei!")
    exit(1)  # Beendet das Skript, bevor Discord.py abstürzt
bot.run(token)