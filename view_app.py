import sqlite3

def show_visits():
    conn = sqlite3.connect('visits.db')
    c = conn.cursor()

    c.execute('SELECT id, collected_on, url FROM visits')
    visits = c.fetchall()

    print("\nVisits:")
    for visit in visits:
        print(f"{visit[0]}: {visit[1]} {visit[2]}")

    conn.close()
    return [v[0] for v in visits]

def show_visit_items(visit_id):
    conn = sqlite3.connect('visits.db')
    c = conn.cursor()

    c.execute('''
        SELECT id, name, rank
        FROM visit_items
        WHERE visit_id = ?
        ORDER BY rank ASC
    ''', (visit_id,))
    items = c.fetchall()

    print("\nVisit items:")
    print("ITEM ID | NAME                          | RANK")
    print("-----------------------------------------------")
    for item in items:
        print(f"{item[0]:<7} | {item[1]:<30} | {item[2]}")

    conn.close()
    return [item[0] for item in items]

def show_item_details(item_id):
    conn = sqlite3.connect('visits.db')
    c = conn.cursor()

    # Haal item naam op
    c.execute('SELECT name FROM visit_items WHERE id = ?', (item_id,))
    item = c.fetchone()
    if not item:
        print("Item niet gevonden.")
        return

    print(f"\nDetails for '{item[0]}':")

    # Haal alle key/value info op
    c.execute('''
        SELECT key, value
        FROM visit_item_info
        WHERE visit_item_id = ?
    ''', (item_id,))
    info = c.fetchall()

    if not info:
        print("Geen extra informatie beschikbaar.")
    else:
        for k, v in info:
            print(f"- {k}: {v}")

    conn.close()

def main():
    while True:
        valid_visit_ids = show_visits()
        print("\nKies een visit nummer om de items te tonen, of X om te stoppen.")
        visit_choice = input("Keuze: ").strip()

        if visit_choice.lower() == 'x':
            break
        elif visit_choice.isdigit() and int(visit_choice) in valid_visit_ids:
            visit_id = int(visit_choice)
            while True:
                valid_item_ids = show_visit_items(visit_id)
                print("\nKies een ITEM ID om details te bekijken, of B om terug te gaan.")
                item_choice = input("Keuze: ").strip()

                if item_choice.lower() == 'b':
                    break
                elif item_choice.isdigit() and int(item_choice) in valid_item_ids:
                    show_item_details(int(item_choice))
                    input("\nDruk op Enter om terug te gaan naar de lijst met items.")
                else:
                    print("Ongeldige keuze.\n")
        else:
            print("Ongeldige keuze.\n")

if __name__ == "__main__":
    main()

