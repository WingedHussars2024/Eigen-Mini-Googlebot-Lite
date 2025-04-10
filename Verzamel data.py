import requests
from bs4 import BeautifulSoup

# URL van de IMDB Top 250 pagina
url = 'https://www.imdb.com/chart/top/'
headers = {
"User-Agent": "Mozilla/5.0",
"Accept": "application/json"
}

# Verstuur een GET-request naar de pagina
response = requests.get(url, headers=headers)

# Check of de request succesvol was
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Zoek alle filmtitels en hun rang
    movies = soup.select('li.ipc-metadata-list-summary-item')

    # Loop door de films en print de naam en rang
    for index, movie in enumerate(movies, start=1):
        title_tag = movie.select_one('h3')
        if title_tag:
            title = title_tag.text.strip()
            print(f"{title} staat op {index}")
else:
    print(f"Fout bij het ophalen van de pagina: {response.status_code}")
