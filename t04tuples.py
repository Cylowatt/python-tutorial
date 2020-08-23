# Tuples are immutable sequences.
from collections import namedtuple


def make_tuple():
    tuple_via_constructor = tuple(['United Kingdom', 'London', 60_000_000])

    # Parentheses are optional.
    two_item_tuple = 'first', 'second'

    this_is_a_string = ('str')
    this_is_a_tuple = ('str',)
    empty_tuple = ()

    return ('United Kingdom', 'London', 60_000_000)


def make_named_tuple():
    NamedTupleClass = namedtuple('ClassName', 'country, capital, population')

    instance = NamedTupleClass('Japan', 'Tokyo', 120_000_000)

    # Access members by name or index.
    country = instance[0]
    capital = instance.capital

    return instance


def tuple_operations():
    print("\nTuple Operations")

    t = make_tuple()

    # Concatenation.
    t2 = t + t

    print(t2)

    # Equality. Compares items from the left.
    equal = t == t2

    to_insert_into_dict = hash(t)

    # Iteration.
    for item in make_named_tuple():
        print(item)

    # Repetition.
    t2 = t * 10


def tuple_methods():
    tuple = make_tuple()

    # Count item.
    print(tuple.count('London'))

    # Find the index of some value or throw ValueError.
    print(tuple.index('United Kingdom'))
