import sqlite3
from datetime import datetime

def insert_visit(url, items):
    conn = sqlite3.connect('visits.db')
    c = conn.cursor()

    # Huidige timestamp
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

    # Voeg bezoek toe
    c.execute('INSERT INTO visits (collected_on, url) VALUES (?, ?)', (timestamp, url))
    visit_id = c.lastrowid

    # Voeg items toe
    for rank, name in enumerate(items, start=1):
        c.execute('INSERT INTO visit_items (visit_id, name, rank) VALUES (?, ?, ?)', (visit_id, name, rank))

    conn.commit()
    conn.close()
    print(f"Visit en {len(items)} items toegevoegd.")

if __name__ == "__main__":
    # Simuleer een lijst van bordspellen
    games = [
        "The Shawshank Redemption",
        "The Godfather",
        "The Dark Night",
        "The Godfather Part II",
        "De 12 gezworenen"
    ]
    url = "https://www.imdb.com/chart/top/"
    insert_visit(url, games)

