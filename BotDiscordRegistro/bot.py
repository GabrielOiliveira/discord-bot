import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# Carrega o .env na pasta do script
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True

class MeuBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

bot = MeuBot()

@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}")

@bot.event
async def on_member_join(member):
    guild = member.guild
    canal_registro = discord.utils.get(guild.text_channels, name="registro")
    
    if canal_registro:
        
        await canal_registro.send(
            f"👋 Olá {member.mention}, seja bem-vindo!\n"
            f"Para acessar o servidor, digite o comando:\n"
            f"`/registrar seu_nick#123456`\n\n"
            f"Exemplo: `/registrar Nick#123456`"
        )

@bot.tree.command(name="registrar", description="Registra seu nome e libera o servidor.")
@app_commands.describe(apelido="Digite seu nick no formato: Nick#123456")
async def registrar(interaction: discord.Interaction, apelido: str):
    if "#" not in apelido:
        await interaction.response.send_message("❌ Formato inválido! Use assim: Nick#123456", ephemeral=True)
        return

    try:
        await interaction.user.edit(nick=apelido)
    except discord.Forbidden:
        await interaction.response.send_message("❌ Não posso alterar seu apelido. Verifique minhas permissões.", ephemeral=True)
        return

    cargo = discord.utils.get(interaction.guild.roles, name="Membro")
    if not cargo:
        await interaction.response.send_message("❌ Cargo 'Membro' não encontrado.", ephemeral=True)
        return

    await interaction.user.add_roles(cargo)
    await interaction.response.send_message(f"✅ Pronto, {apelido}! Agora você tem acesso ao servidor.", ephemeral=True)

bot.run(TOKEN)
