from matchers import All, And, PlaysIn


class QueryBuilder:
    def __init__(self, query=All()):
        self.query_object = query

    def plays_in(self, team):
        return QueryBuilder(And(self.query_object, PlaysIn(team)))

    def build(self):
        return self.query_object
