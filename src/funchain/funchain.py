from collections import abc
import itertools
from typing import Iterator, overload, Optional, Callable, TypeVar, Tuple, Sequence

T = TypeVar('T')
S = TypeVar('S')


class Chain(abc.Iterator):
    def __init__(self, start_it: Iterator):
        self.it = start_it

    def filter(self, fun: Callable[[T], bool]) -> 'Chain':
        self.it = filter(fun, self.it)
        return self

    def map(self, fun: Callable[[T], S]) -> 'Chain':
        self.it = map(fun, self.it)
        return self

    def map_by(self, fun: Callable[[Iterator], Iterator]) -> 'Chain':
        self.it = fun(self.it)
        return self

    def sorted(self, *, key=None, reverse=False) -> Sequence[T]:
        """
        Sorts the iterator.

        It relies on the buildin method `sorted`. It means in the backend it generates a list.
        Hence the iterator will be evaluated and a list is assigned.
        """
        return sorted(self.it, key=key, reverse=reverse)

    @overload
    def islice(self, stop: int) -> 'Chain': ...
    @overload
    def islice(self, start: int, stop: int, step: Optional[int]) -> 'Chain': ...

    def islice(self, item, stop=None, step=None):
        if stop is None:
            self.it = itertools.islice(self.it, item)
        else:
            self.it = itertools.islice(self.it, item, stop, step)
        return self

    def takewhile(self, predicate: Callable[[T], bool]) -> 'Chain':
        self.it = itertools.takewhile(predicate, self.it)
        return self

    def tee(self, n=2) -> Tuple['Chain', ...]:
        results = itertools.tee(self.it, n)
        return tuple(Chain(r) for r in results)

    def __next__(self):
        return self.it.__next__()
