#!/usr/bin/python3
import sys
import calculator_1

operators = ["+", "-", "*", "/"]

operand = sys.argv[1:]


def calculate():
    argv_len = len(sys.argv) - 1
    if argv_len < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if operand[1] in operators:
        if operand[1] == "+":
            sum = calculator_1.add(int(operand[0]), int(operand[2]))
            print("{} + {} = {}".format(operand[0], operand[2], sum))
            exit(0)
        elif operand[1] == "-":
            sub = calculator_1.sub(int(operand[0]), int(operand[2]))
            print("{} + {} = {}".format(operand[0], operand[2], sub))
            exit(0)
        elif operand[1] == "*":
            mul = calculator_1.mul(int(operand[0]), int(operand[2]))
            print("{} + {} = {}".format(operand[0], operand[2], mul))
            exit(0)
        else:
            div = calculator_1.div(int(operand[0]), int(operand[2]))
            print("{} + {} = {}".format(operand[0], operand[2], div))
            exit(0)
    else:
        print("nknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == '__main__':
    calculate()
