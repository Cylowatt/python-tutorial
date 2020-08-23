# File Modes
# r - read text file (default)
# w - write text file (truncates if exists)
# x - write text file (throw FileExistsError if exists)
# a - append to text file (write to end)
#
# rb - read binary file
# wb - write binary (truncate)
# w+b - open binary file for reading and writing
# xb - write binary file (throw FileExistsError if exists)
# ab - append to binary file (write to end)
#
# Check file methods in reference.

def read_files():
    with open('./test_file.txt') as fin:
        for line in fin:
            print(repr(line))


def write_to_files():
    with open('./test_file.txt', 'w') as fout:
        fout.write("Hi There")
