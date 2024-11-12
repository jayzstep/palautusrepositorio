class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        nation_players = [
            player for player in self.players if player.nationality == nationality
        ]
        nation_players.sort(
            key=lambda player: (-(player.goals + player.assists), player.name)
        )
        return nation_players

    def get_nationalities(self):
        nations = [
            player.nationality for player in self.players
        ]
        set_nations = set(nations)
        return set_nations


# omg
