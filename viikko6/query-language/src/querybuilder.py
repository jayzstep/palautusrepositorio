from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, query=All()):
        self.query_object = query

    def plays_in(self, team):
        return QueryBuilder(And(self.query_object, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.query_object, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.query_object, HasFewerThan(value, attr)))

    def one_of(self, query1, query2):
        return QueryBuilder(And(self.query_object, Or(query1, query2)))

    def build(self):
        return self.query_object
