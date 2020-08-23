# Set - mutable unordered collection that cannot contain duplicates.

def sets():
    # Useful for removing duplicates and quick membership tests.
    nums = [1, 2, 3, 1]
    num_set = set(nums)

    is_3_in_set = 3 in num_set

    num_set_2 = {3, 4, 5, 6}

    # Set operations.
    union = num_set | num_set_2
    intersection = num_set & num_set_2
    difference = num_set - num_set_2
    xor = num_set ^ num_set_2

    empty_set = set()

def set_operations():
    set = {1, 2, 3}
    set_2 = {1, 2, 3, 4, 5}

    is_set_2_superset_of_set = set >= set_2
    is_set_2_strict_superset_of_set = set > set_2

    # See reference for more set operations.