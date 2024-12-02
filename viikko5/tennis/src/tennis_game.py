class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    MIN_FOR_WIN = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def handle_tie(self):
        if self.player1_points == self.LOVE:
            return "Love-All"
        if self.player1_points == self.FIFTEEN:
            return "Fifteen-All"
        if self.player1_points == self.THIRTY:
            return "Thirty-All"
        return "Deuce"

    def handle_advantage(self):
        difference = self.player1_points - self.player2_points

        if difference == 1:
            return "Advantage player1"
        if difference == -1:
            return "Advantage player2"
        if difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def handle_score(self):
        point_names = {
            self.LOVE: "Love",
            self.FIFTEEN: "Fifteen", 
            self.THIRTY: "Thirty",
            self.FORTY: "Forty"
        }
        return f"{point_names[self.player1_points]}-{point_names[self.player2_points]}"

    def get_score(self):
        if self.player1_points == self.player2_points:
            return self.handle_tie()
        if self.player1_points >= self.MIN_FOR_WIN or self.player2_points >= self.MIN_FOR_WIN:
            return self.handle_advantage()
        return self.handle_score()
