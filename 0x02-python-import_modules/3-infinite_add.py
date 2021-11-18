#!/usr/bin/python3

if __name__ == "__main__":
    # Import modules
    import sys

    # prints the results of the addition of the arguments
    # print(sum(int(arg) for arg in sys.argv[1:]))
    sum = 0

    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])

    print("{:d}".format(sum), end="")
