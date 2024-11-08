import requests

from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    seasons = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
    ]
    season = input("Select season:")
    if season in seasons:
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
    else:
        print("byee!")
        return

    nationalities = stats.get_nationalities()

    while True:
        nationality = input("nationality: ")
        if nationality in nationalities:
            players = stats.top_scorers_by_nationality(nationality)
            for player in players:
                print(player)
        break


if __name__ == "__main__":
    main()
