import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_loytaa_pelaajan(self):
        result = self.stats.search("Semenko")

        self.assertEqual(str(result), "Semenko EDM 4 + 12 = 16")

    def test_search_palauttaa_none_jos_ei_pelaajaa(self):

        result = self.stats.search("Selänne")

        self.assertEqual(str(result), "None")

    def test_team_palauttaa_oikean_maaran_pelaajia(self):
        result = self.stats.team("EDM")

        self.assertEqual(len(result), 3)

    def test_top_palauttaa_eniten_pisteita(self):
        result = self.stats.top(2)

        self.assertEqual(result[0].name, "Gretzky")

    def test_top_palauttaa_eniten_syottoja(self):
        result = self.stats.top(2, SortBy.ASSISTS)

        self.assertEqual(result[1].name, "Yzerman")

    def test_top_palauttaa_eniten_maaleja(self):
        result = self.stats.top(2, SortBy.GOALS)

        self.assertEqual(result[0].name, "Lemieux")
