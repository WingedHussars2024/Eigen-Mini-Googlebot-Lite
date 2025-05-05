import sqlite3
from datetime import datetime

def insert_visit(url, items_with_info):
    conn = sqlite3.connect('visits.db')
    c = conn.cursor()

    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
    c.execute('INSERT INTO visits (collected_on, url) VALUES (?, ?)', (timestamp, url))
    visit_id = c.lastrowid

    for rank, item in enumerate(items_with_info, start=1):
        name = item["name"]
        c.execute('INSERT INTO visit_items (visit_id, name, rank) VALUES (?, ?, ?)', (visit_id, name, rank))
        visit_item_id = c.lastrowid

        # Extra info (key-value paren)
        for key, value in item["extra"].items():
            c.execute('INSERT INTO visit_item_info (visit_item_id, key, value) VALUES (?, ?, ?)',
                      (visit_item_id, key.upper(), str(value)))

    conn.commit()
    conn.close()
    print(f"Visit en {len(items_with_info)} items toegevoegd.")


if __name__ == "__main__":
    items = [
        {
            "name": "The Shawshank Redemption",
            "extra": {
                "year": 1994,
                "imbd rating": 9.3,
                "description": "A banker convicted of uxoricide forms a friendship over a quarter century with a hardened convict, while maintaining his innocence and trying to remain hopeful through simple compassion."
            }
        },
        {
            "name": "The Godfather",
            "extra": {
                "year": 1972,
                "imbd rating": 9.2,
                "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
            }
        }
    ]
    url = "https://www.imdb.com/chart/top/"
    insert_visit(url, items)


