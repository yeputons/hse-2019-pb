from typing import List
import sys
def main(argv: List[str]):
    s = 0
    for arg in argv:
        for val in arg.split(','):
            s += int(val)
        print(s)
if __name__ == '__main__':
    main(sys.argv[1:])
