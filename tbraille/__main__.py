import argparse
import sys
from . import tbraille


parser = argparse.ArgumentParser()

parser.add_argument(
    '-f', '--font',
    default=None,
    help='Font name')
parser.add_argument(
    '-s', '--size',
    type=int,
    default=20,
    help='Font size')
parser.add_argument(
    'text',
    nargs='?'
)


def main():
    args = parser.parse_args()
    text = args.text
    if not text:
        text = sys.stdin.read()
    text = text.strip()
    print(tbraille(args.font, args.size, text))


if __name__ == '__main__':
    main()
