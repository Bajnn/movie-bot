import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os
import requests
load_dotenv()

intents = disnake.Intents.all()
activity = disnake.Activity(
    name="Simple movie bot",
    type=disnake.ActivityType.playing,
)
bot = commands.Bot(intents=intents, command_prefix="!", activity=activity)


def embeder(movie_id):
    embed = f"https://vidsrc.to/embed/movie/{movie_id}"
    return embed
def get_movie(name):
    url = f"https://v3.sg.media-imdb.com/suggestion/x/{name}.json?includeVideos=1"
    response = requests.get(url)
    json_data = response.json()
    movies = json_data.get("d", [])
    if movies:
        first_movie = movies[0]
        movie_id = first_movie.get("id")
        movie_title = first_movie.get("l")
        return movie_id, movie_title
        
    return None
@bot.slash_command(name="film")
async def find_film(interaction, movie: str):
    id, title = get_movie(movie)
    link = embeder(id)
    embed = disnake.Embed(title=title, description=f"[watch here](<{link}>)")
    
    
    await interaction.send(embed=embed)

bot.run(os.getenv("TOKEN"))

