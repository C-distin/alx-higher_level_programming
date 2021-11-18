#!/usr/bin/python3

if __name__ == "__main__":

    # Import modules
    import sys
    import argparse

    # print number of arguments and length of each argument
    args = len(sys.argv) - 1

    if args == 0:
        print("{} arguments".format(args))

    elif args == 1:
        print("{} argument:".format(args))

    else:
        print("{} arguments:".format(args))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
