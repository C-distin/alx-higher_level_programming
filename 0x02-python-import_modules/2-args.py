#!/usr/bin/python3

if __name__ == "__main__":

    # Import modules
    import sys
    import argparse

    # print number of arguments and length of each argument
    args = len(sys.argv) - 1

    if args == 0:
        print("{:d} arguments".format(args), end="")

    elif args == 1:
        print("{:d} argument:".format(args), end="")

    else:
        print("{:d} arguments:".format(args), end="")

    for i in range(1, len(sys.argv)):
        print("{:d}: {:d}".format(i, sys.argv[i]),)
