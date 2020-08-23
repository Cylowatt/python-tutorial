# See https://docs.python.org/3/howto/functional.html
def functional_programming():
    list_list = ['  line 1\n', 'line 2  \n', 'line 3 \n']

    # Generator expression. Returns iterator.
    stripped_iter = (line.strip() for line in list_list if line != "")
    print(stripped_iter)

    # List comprehension. Returns list.
    stripped_list = [line.strip() for line in list_list if line != ""]
    print(stripped_list)

    # Combining sequences.
    seq1 = 'abc'
    seq2 = (1, 2, 3)

    combined = [(x, y) for x in seq1 for y in seq2]
    print(combined)

    for i in generator():
        print(i)


def generator():
    for i in range(8):
        yield i


def built_in_functions():
    # map(f, iterA, iterB, ...)
    print(list(map(lambda v: v + 5, range(3))))

    # Same with list comprehension.
    print(list(x + 5 for x in range(3)))

    # filter(predicate, iter)
    # Get only even numbers.
    print(list(filter(lambda x: x % 2 == 0, range(10))))

    # enumerate(iter, start=0)
    # Returns iterable of tuples (index, element)
    #
    # Useful for looping through a list and recoding
    # indexes at which certain conditions are met.
    print(list(enumerate(['subject', 'object', 'verb'])))

    # sorted(iterable, key=None, reverse=False)
    print(list(sorted(['c', 'a', 'b'])))

    # any(iter) return true if any element in the iterable is a true value.
    # all(iter) returns true is all elements in the iterable are true values.
    print(any([1, 0, 0]))
    print(all([1, 1, 1]))

    # zip(iterA, iterB, ...) takes one element from each
    # iterable and returns them in a tuple.
    #
    # Lazy evaluated. Iterator lengths should match.
    # If they do not, the shortest one is returned.
    print(list(zip([1, 2, 3], ('a', 'b', 'c'))))

    # More functions in itertools and functools modules.


def default_values(n=42):
    print(n)


def positional_args(*args):
    for arg in args:
        print(arg)


def keyword_args(**kwargs):
    for key in kwargs:
        print(f'{key} - {kwargs[key]}')


def keyword_only_parameters(*, x1=0, y1=0, x2=0, y2=0):
    return x1 + x2, y1 + y2


def unpacking_arguments():
    # Same as ... spread operator in JS.
    t = (2, 5)
    d = {"this": 3, "that": 1}

    # print(*t)
    # print(**d)

# Comprehensions over lists, sets, dictionaries, generators, and also async.
