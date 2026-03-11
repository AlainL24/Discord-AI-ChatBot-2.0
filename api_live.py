import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Weather API
def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()
    if res.get("cod") != 200:
        return f"Weather info not found for {city}."
    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]
    return f"The current weather in {city} is {temp}°C with {desc}."

# NBA Scores API (balldontlie free API)
def get_top_nba_scorer():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    url = f"https://www.balldontlie.io/api/v1/stats?dates[]={today}&per_page=100"
    res = requests.get(url).json()
    if not res["data"]:
        return "No NBA games found today."
    top_player = max(res["data"], key=lambda x: x["pts"])
    return f"{top_player['player']['first_name']} {top_player['player']['last_name']} scored {top_player['pts']} points today."