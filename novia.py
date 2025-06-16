import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),
    help_command=None  # Opcional: Desactiva el comando !help por defecto
)

# Obtener configuración de .env
TOKEN = os.getenv("DISCORD_TOKEN")
ROL_ID = int(os.getenv("ROL_ID"))  # Convertir a entero

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.event
async def on_message(message: disnake.Message):
    if bot.user.mentioned_in(message) and not message.author.bot:
        guild = message.guild
        member = message.author
        role = guild.get_role(ROL_ID)

        if not role:
            await message.channel.send("No existe rol furro :(.")
            return

        if role in member.roles:
            try:
                await member.remove_roles(role)
                embed = disnake.Embed(
                    title="Furrificacion 🐱",
                    description=f"tu amor a los furros fue tan fuerte que tuve que quitartelos",
                    color=disnake.Color.green()
                )
                await message.channel.send(embed=embed)
            except disnake.Forbidden:
                await message.channel.send("😿 No puedo hacer eso.")
            except Exception as e:
                await message.channel.send(f"❌ **Error:** {str(e)}")
        else:
            await message.channel.send(f"😾 No eres furro")
    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(TOKEN)
