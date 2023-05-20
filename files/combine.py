#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Combine files and ensure that each file used terminates with a line break')
    parser.add_argument('output_file', type=argparse.FileType('w'))
    parser.add_argument('input_filenames', nargs='+')
    args = parser.parse_args()
    output = args.output_file
    for filename in args.input_filenames:
        text = open(filename).read()
        if text[-1] != '\n':
            text += '\n'
        output.write(text)
    output.close()
