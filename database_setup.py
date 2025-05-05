import sqlite3

def setup_database():
    conn = sqlite3.connect('visits.db')
    c = conn.cursor()

    # Maak de visits tabel
    c.execute('''
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            collected_on TEXT,
            url TEXT
        )
    ''')

    # Maak de visit_items tabel
    c.execute('''
        CREATE TABLE IF NOT EXISTS visit_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            visit_id INTEGER,
            name TEXT,
            rank INTEGER,
            FOREIGN KEY(visit_id) REFERENCES visits(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database en tabellen aangemaakt.")

