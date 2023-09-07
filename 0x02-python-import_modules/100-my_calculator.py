#!/usr/bin/python3.8

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if (len(argv) != 4):
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    op = argv[2]
    a = int(argv[1])
    b = int(argv[2])
    if (op == "+"):
        result = add(a, b)
    elif (op == "-"):
        result = sub(a, b)
    elif (op == "/"):
        result = div(a, b)
    elif (op == "*"):
        result = mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
