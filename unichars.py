#!/usr/bin/env python3
"""
Decode unicode input
"""
import fileinput
import sys
import unicodedata

def format_char(char):
    name = unicodedata.name(char, "[name missing]")
    return f'U+{ord(char):0>4X}\t{name}'

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in {'-h', '--help'}:
        print(f"usage: unichars [-h|--help] [file ...]",
              "  Display information about the characters given as input.",
              "  With no arguments, prompt for one line of input.",
              "  With arguments, use the files as input, with '-' as stdin.",
              sep='\n', file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) > 1:
        with fileinput.input() as files:
            for line in files:
                for char in line:
                    print(format_char(char))
    else:
        for char in input("Enter string: "):
            print(format_char(char))
