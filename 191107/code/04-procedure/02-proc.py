from typing import List
import sys
def process(arg: str):
    s = 0
    for val in arg.split(','):
        s += int(val)
    print(s)
def main(argv: List[str]):
    for arg in argv:
        process(arg)
if __name__ == '__main__':
    main(sys.argv[1:])
