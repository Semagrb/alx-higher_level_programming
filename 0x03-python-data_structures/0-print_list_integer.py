#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    for item in my_list:
        if isinstance(item, int):
            print("{:d}".format(item))

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, "Not an integer", 6]
    print_list_integer(my_list)
