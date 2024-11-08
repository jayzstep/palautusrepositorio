import requests

from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()
    nationality = "FIN"

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    nationality_players = [
        player for player in players if player.nationality == nationality
    ]
    nationality_players.sort(
        key=lambda player: (-(player.goals + player.assists), player.name)
    )

    print(f"Players from {nationality}:\n")

    for player in nationality_players:
        print(player)


if __name__ == "__main__":
    main()
