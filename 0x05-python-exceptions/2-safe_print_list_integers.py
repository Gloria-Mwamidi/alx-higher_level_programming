#!/bin/usr/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    a function that prints the first x elements of
    a list and only integers.
    Returns the real number of integers printed
    """
    result = 0
    for i in range(x,0):
        try:
            print("{:d}".format(my_list[i]), end="")
            result += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (result)
