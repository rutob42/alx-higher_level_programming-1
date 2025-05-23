#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if not isinstance(size, (float)) and size < 0:
        raise TypeError("size must be >= 0")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
