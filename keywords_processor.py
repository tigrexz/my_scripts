#!/usr/bin/env python3
import re
import argparse

def main():
    # create argument parser
    parser = argparse.ArgumentParser()
    # add arguements
    parser.add_argument('-f', '--filename', dest='f', type=str, required=True, help="Input file's filename")

    # parse arguments
    args = parser.parse_args()

    # create file object
    filename = str(args.f)
    # create regex object
    reg1 = re.compile(r'(\w+[^\S\r\n]?\w+)[\n\r,:\."\']*')  # works for text with one line or mutiple lines

    try:
        with open(filename) as file:
            keywords = file.read()
        # create match object
        mo1 = reg1.findall(keywords)

        str1 = ''
        for i in mo1:
            str += f'\"{i}\" OR '

        print('\n')
        print("The keywords that need to be processed are:\n\n", keywords)
        print("\nThe processed keywords are:\n\n", str1.rstrip(' OR'))
        print('\n')
    except FileNotFoundError:
        print(f"Sorry, {filename} does not exist!")


if __name__ == "__main__":
    main()
