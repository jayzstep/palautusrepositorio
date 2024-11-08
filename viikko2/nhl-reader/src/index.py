import requests
from rich.console import Console
from rich.table import Table
console = Console()
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
    season = console.input("Select season:")
    if season in seasons:
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
    else:
        console.print("byee!", style="bold red")
        return

    nationalities = stats.get_nationalities()

    while True:
        nationality = console.input("nationality: ")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name")
        table.add_column("Team")
        table.add_column("Goals")
        table.add_column("Assists")
        table.add_column("Points")
        if nationality in nationalities:
            players = stats.top_scorers_by_nationality(nationality)
            for player in players:
                table.add_row(
                    str(player.name),
                    str(player.team),
                    str(player.goals),
                    str(player.assists),
                    str(player.goals + player.assists)
                )
        if nationality == "exit":
            break
        console.print(table)


if __name__ == "__main__":
    main()
