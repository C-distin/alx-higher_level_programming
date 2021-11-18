#!/usr/bin/python3

# Import the add() function from the file add_0.py
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    # Call the add() function from the add_0.py file
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)), end="")
