def show_okc_stats():
    stats_text = """
2025-26 Regular Season
2024-25 Postseason
2024-25 Regular Season
2023-24 Postseason
2023-24 Regular Season
put ALL the text you pasted here ...
1.336
0.56
"""
    print(stats_text)


def main():
    while True:
        print("🏀 Thunder Stats Menu 🏀")
players = [
    {
        "name": "Shai Gilgeous-Alexander",
        "GP": 54,
        "GS": 54,
        "MIN": 33.5,
        "PTS": 31.7,
        "OR": 0.5,
        "DR": 4.0,
        "REB": 4.5,
        "AST": 6.6,
        "STL": 1.4,
        "BLK": 0.8,
        "TO": 2.1,
        "PF": 2.0,
        "AST_TO": 3.1,
    },
    {
        "name": "Jalen Williams",
        "GP": 26,
        "GS": 26,
        "MIN": 29.0,
        "PTS": 17.5,
        "OR": 0.7,
        "DR": 4.0,
        "REB": 4.7,
        "AST": 5.4,
        "STL": 1.3,
        "BLK": 0.3,
        "TO": 1.9,
        "PF": 2.1,
        "AST_TO": 2.8,
    },
    {
        "name": "Chet Holmgren",
        "GP": 56,
        "GS": 56,
        "MIN": 29.3,
        "PTS": 17.3,
        "OR": 1.9,
        "DR": 7.1,
        "REB": 9.0,
        "AST": 1.8,
        "STL": 0.5,
        "BLK": 1.9,
        "TO": 1.6,
        "PF": 2.3,
        "AST_TO": 1.1,
    },
    # add more players here...
]


def print_all_players_stats():
    print("OKC 2025-26 Player Stats:\n")
    for p in players:
        print(f"{p['name']}:")
        print(f"  GP: {p['GP']}, GS: {p['GS']}, MIN: {p['MIN']}")
        print(f"  PTS: {p['PTS']}, REB: {p['REB']} (OR {p['OR']}, DR {p['DR']}), AST: {p['AST']}")
        print(f"  STL: {p['STL']}, BLK: {p['BLK']}, TO: {p['TO']}, PF: {p['PF']}, AST/TO: {p['AST_TO']}")
        print()  # blank line between players


def main():
    while True:
        print("1. Show all OKC player stats")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")

        if choice == "1":
            print_all_players_stats()
        elif choice == "2":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
