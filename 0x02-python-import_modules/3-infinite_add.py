#!/usr/bin/python3
if __name__ == "__main__":
    """Print a summation of all the arguments"""
    from sys import argv
    total_sum = 0
    for arg in (argv[1:]):
        total_sum += int(arg)
    print(f"{total_sum}")
