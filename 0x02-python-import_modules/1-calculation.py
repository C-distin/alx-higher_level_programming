#!/usr/bin/python3

# Import the calculator module from the calculator_1.py file
if __name__ == "__main__":
    import calculator_1 as calc

    a = 10
    b = 5

    # Call the add() function from the calculator module
    print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))

    # Call the sub() function from the calculator module
    print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))

    # Call the mul() function from the calculator module
    print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))

    # Call the div() function from the calculator module
    print("{:d} / {:d} = {:d}".format(a, b, calc.div(a, b)))
