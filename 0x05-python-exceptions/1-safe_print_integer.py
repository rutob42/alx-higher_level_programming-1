#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if (type(value) == int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except IndexError:
        print()         1aq     swwde4
