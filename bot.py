import discord
from discord import app_commands
import os
from dotenv import load_dotenv

from research import search_sources
from ai import generate_answer
from api_live import get_weather, get_top_nba_scorer

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)
    synced = await tree.sync(guild=guild)
    print(f"Synced {len(synced)} command(s)")
    print(f"Logged in as {client.user}")

@tree.command(
    name="ask",
    description="Ask Cloud AI a question",
    guild=discord.Object(id=GUILD_ID)
)
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.send_message(f"🔎 **Researching your question...**\n\n**Question:** {question}")

    try:
        lower_q = question.lower()

        # Live APIs
        if "weather" in lower_q:
            city = question.split("in")[-1].strip() if "in" in lower_q else ""
            answer = get_weather(city)
            sources = [{"title": "OpenWeatherMap", "url": "https://openweathermap.org"}]
        elif "nba" in lower_q or "basketball" in lower_q:
            answer = get_top_nba_scorer()
            sources = [{"title": "balldontlie API", "url": "https://www.balldontlie.io/"}]
        else:
            sources = search_sources(question)
            answer = generate_answer(question, sources)

        source_links = "\n".join([f"- {s['url']}" for s in sources])
        response = f"""
**Question**
{question}

**Answer**
{answer}

**Sources**
{source_links}
"""
        await interaction.edit_original_response(content=response)
    except Exception as e:
        print(e)
        await interaction.edit_original_response(content="I’m currently unable to retrieve the information. Please try again later.")

client.run(TOKEN)