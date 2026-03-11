import discord
from discord import app_commands
import os
from dotenv import load_dotenv

from research import search_sources
from ai import generate_answer

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():

    guild = discord.Object(id=GUILD_ID)

    try:
        synced = await tree.sync(guild=guild)
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    print(f"Logged in as {client.user}")


@tree.command(
    name="ask",
    description="Ask Cloud AI a question",
    guild=discord.Object(id=GUILD_ID)
)
async def ask(interaction: discord.Interaction, question: str):

    # STEP 1 — show researching message
    await interaction.response.send_message(
        f"🔎 **Researching your question...**\n\n**Question:** {question}"
    )

    try:

        # STEP 2 — search
        search_query = f"{question} latest news 2026"

        sources = search_sources(search_query)

        # STEP 3 — AI answer
        answer = generate_answer(question, sources)

        # STEP 4 — format sources
        source_links = "\n".join(
            [f"- {s['url']}" for s in sources]
        )

        response = f"""
**Question**
{question}

**Answer**
{answer}

**Sources**
{source_links}
"""

        # STEP 5 — edit original message
        await interaction.edit_original_response(content=response)

    except Exception as e:

        print(e)

        await interaction.edit_original_response(
            content="I’m currently unable to retrieve the information. Please try again later."
        )


client.run(TOKEN)