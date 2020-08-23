import t03dictionaries
import t10decorators
import t11coroutines
import t00shapes
import t01variables
from t04tuples import tuple_operations, tuple_methods
from t06functionalprogramming import functional_programming, built_in_functions
from t07files import read_files, write_to_files


def run():
    t00shapes.draw_triangle()
    t01variables.variables()
    t01variables.numbers()
    t01variables.number_magic_methods()
    t03dictionaries.dictionary_usage()
    tuple_operations()
    tuple_methods()
    functional_programming()
    built_in_functions()
    read_files()
    write_to_files()
    t10decorators.subtract(5, 10)
    t11coroutines.coroutines()


if __name__ == '__main__':
    run()
