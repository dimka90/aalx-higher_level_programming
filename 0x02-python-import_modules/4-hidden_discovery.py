#!/usr/bin/python3

def main():
    import hidden_4
    # the dir function shows all the function and packeges that
    # a certain module used
    modules = dir(hidden_4)
    for module in modules:
        # The if statement  slice the first two letters of each module
        # it checks to see if it contains a double underscore
        if module[0:2] != '__':
            print(module)


if __name__ == "__main__":
    main()
