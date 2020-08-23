# Comments start with the hash symbol. There are no multiline comments.
import math


def variables():
    s = 'some string'
    n = 42
    print(s)
    print(n)


def numbers():
    integer = 14
    hex = 0xe
    octal = 0o16
    binary = 0b1110
    float = 14.0
    float = 14e1
    complex = 14 + 0j
    underscore = 1_000


def number_magic_methods():
    abs(50)
    bool(1)

    # Integer division.
    x = 5 // 2

    # Float division
    x = 5 / 2

    # Integer conversion.
    int(50.5)

    twenty_five = 5 ** 2
    round(3.14)

    # String conversion.
    str(4.3)

    # Truncation.
    math.trunc(5.2)

    # Floating point equality testing.
    math.isclose(5.2, 5.2)


def integer_magic_methods():
    math.ceil(5.2)
    math.floor(5.2)

    # Number of bits necessary.
    t = 5
    t.bit_length()


def float_magic_methods():
    x = 5.2
    y = x.as_integer_ratio()
    hex = x.hex()
    y = float.fromhex(hex)


# Python 3 strings hold unicode data.
# You can use both ' and " for defining strings.
def strings():
    s = "hello\tthere"

    raw_string = r'hello'
    byte_string = b'hello'


def string_operations():
    s = "foo bar"

    # Membership check.
    is_foo = "foo" in s

    length = len(s)

    # Programmer-friendly string.
    repr(s)

    # User-friendly string.
    str(s)

    # String interpolation.
    s = f'hi {s} there'

    # Strings contain a whole bunch of methods.

    # String format supports conversion flags.
    # !s - calls str() on argument.
    # !r - calls repr() on argument.
    # !a - calls ascii() on argument.
    print("{}, {!s} {!a} {!r}".format("a", "a", "a", "a"))