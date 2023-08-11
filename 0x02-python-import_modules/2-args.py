#!/usr/bin/python3
import sys
def main()
    count = 1
    argv_len = len(sys.argv) - 1
    if argv_len == 0:
        print("{} arguments.".format(argv_len))
    elif argv_len == 1:
	print("{} argument:".format(argv_len))
    else:
	print("{} arguments:".format(argv_len))
    for counter in sys.argv[1:]:
	print("{}: {}".format(count, counter))
	count = count + 1
	
if __name__ == "__main__":
    main()
