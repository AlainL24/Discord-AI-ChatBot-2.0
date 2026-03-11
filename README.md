# Cloud AI Discord Bot v2.1

## Overview

Cloud AI Discord Bot is an AI-powered research assistant for Discord. It answers questions using DuckDuckGo searches, Llama3 AI summarization, and live API data for NBA scores and weather.

---

## v2.1 Features (Patch from v2.0)

- **Live NBA scores** using the balldontlie API
- **Live weather** using OpenWeatherMap API
- Maintains **DuckDuckGo + AI summarization** for general questions
- Shows **🔎 Researching your question…**
- Displays **Question and Answer separately**
- Filters out irrelevant/unhelpful sources
- Proper **guild command syncing**
- Fully **.env-based configuration**
- Compatible with **Python 3.10+**

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/discord-ai-bot.git
cd discord-ai-bot

2. Install dependencies:
pip install -r requirements.txt

3. Create a .env file based on .env.example

4. Start Ollama for Llama3:
ollama run llama3

5. Run the bot:
python bot.py

Usage

Use /ask in your Discord server:

/ask what's the weather in Tampa
/ask who is today's top nba scorer
/ask explain quantum computing
Changes from v2.0 to v2.1
Feature	v2.0	v2.1
NBA Scores	Outdated / search-based	Live API (balldontlie)
Weather	Search-based	Live API (OpenWeatherMap)
Answer formatting	Question + answer sometimes merged	Separate Question + Answer
Sources	Sometimes irrelevant	Filtered + reliable sources
Research message	🔎 Researching… sometimes missing	Always shows 🔎 Researching…

Requirements
Python 3.10+
Discord bot token
Ollama Llama3 model
OpenWeatherMap API key

Changes from v2.0 to v2.1
Feature	v2.1
NBA search-based	Live API (balldontlie)
Weather	Live API (OpenWeatherMap)
Answer Separate Question + Answer
Sources	Filtered + reliable sources
Research message Always shows 🔎 Researching…

## Enjoy <3

```
