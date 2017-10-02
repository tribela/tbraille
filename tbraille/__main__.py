import sys
from . import tbraille


def main():
    text = sys.stdin.read().strip()
    print(tbraille(None, None, text))


if __name__ == '__main__':
    main()
