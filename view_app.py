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
    return [v[0] for v in visits]  # Lijst van geldige IDs

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
    print("VISIT ID | ID | NAME                          | RANK")
    print("------------------------------------------------------")
    for item in items:
        print(f"{visit_id:<8} | {item[0]:<2} | {item[1]:<30} | {item[2]}")

    conn.close()

def main():
    while True:
        valid_ids = show_visits()
        print("\nPress visit number to show visit items:")
        print("Press X to exit.")

        user_input = input("Your choice: ").strip()

        if user_input.lower() == 'x':
            break

        if user_input.isdigit() and int(user_input) in valid_ids:
            show_visit_items(int(user_input))
            input("\nPress Enter to go back to visits...\n")
        else:
            print("Invalid input. Try again.\n")

if __name__ == "__main__":
    main()
