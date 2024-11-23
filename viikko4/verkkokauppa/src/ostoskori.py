class Ostoskori:
    def __init__(self):
        self._tuotteet = []

    def lisaa(self, tuote):
        self._tuotteet.append(tuote)

    def poista(self, tuote):
        for t in self._tuotteet:
            if t == tuote:
                self._tuotteet.remove(t)
                break

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
