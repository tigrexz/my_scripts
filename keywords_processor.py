#!/usr/bin/env python3

import re
import argparse

def main():
    # create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='filename', type=str, required=True, help="Keywords file")

    # parse arguments
    args = parser.parse_args()

    # create regex which works for text with one line or mutiple lines
    keyword_regex = re.compile(r'(\w+[^\S\r\n]?\w+)[\n\r,:\."\']*')

    try:
        with open(args.filename) as file:
            keywords = file.read()

        # find the matches
        matches = ''
        match = keyword_regex.findall(keywords)
        for keyword in match:
            matches += '"{}" OR '.format(keyword)

        print("The keywords that need to be processed are:\n\n", keywords)
        print("The processed keywords are:\n\n", matches.rstrip(' OR'))
    except FileNotFoundError:
        print("Keyword file '{}' does not exist.".format(args.filename))


if __name__ == "__main__":
    main()
