import collections
from typing import Iterator


class Chain(collections.Iterator):
    def __init__(self, start_it: Iterator):
        self.it = start_it

    def filter(self, fun) -> 'Pype':
        self.it = filter(fun, self.it)
        return self

    def map(self, fun) -> 'Pype':
        self.it = map(fun, self.it)
        return self

    def map_by(self, fun) -> 'Pype':
        self.it = fun(self.it)
        return self

    def __next__(self):
        return self.it.__next__()

