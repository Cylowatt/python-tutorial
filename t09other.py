from typing import Dict


def other_things():
    a = True
    b = False

    # Actual words instead of &&, ||, and !.
    if a and b or b and not a:
        print('Never')

    # Ternary operator (conditional expression).
    c = 'c' if a else 'a'


def exceptions():
    try:
        result = sum([1, 2, 3]) / 12
    except ZeroDivisionError as e:  # Catch specific exception and assign it to e.
        return None
    except Exception:
        raise  # Rethrow.
    return result


def raise_exception():
    raise ValueError('Lulz')


# Type Annotations. These can be:
# - Built-in classes
# - Third-party classes
# - Abstract base classes
# - Types found in the types module
# - User-defined classes
#
# Python does not do type checking. Use something like mypy (pip install mypy).
# Usage: python3 -m mypy script.py
def add(x: int, y: int) -> float:
    return x + y


# Types can also be specified with a comment.
ages = {}  # type: Dict[str, int]

# The typing module allows to provide hints for:
# - callback functions
# - generic containers
# - the Any type
# To designate a class or function to not type check its annotations,
# use the @typing.no_type_check decorator.

# Modules are files that end in .py. According to PEP 8, the module names should be
# lowercase and have no underscores in words between them.

# Package - directory that has a file named __init__.py. A package can have modules in
# it, as well as subpackages. The __init__.py can be empty or can import code from
# other modules in the package to remove nesting in import statements.