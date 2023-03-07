import re
import argparse
# create argument parser
parser = argparse.ArgumentParser()
# add arguements
parser.add_argument('-f', '--filename', dest='f', type=str, required=True, help="Input file's filename")

# parse arguments
args = parser.parse_args()


filename = str(args.f)
reg1 = re.compile(r'(\w+\s?\w+)[\n\r,:\.]*')    # works for text with one line or mutiple lines

try:
    with open(filename) as file:
        keywords = file.read()


    mo1 = reg1.findall(keywords)
    print('\n')
    print("the keywords need to be processed are:\n", keywords)

    str = ''
    for i in mo1:
        str += f'\"{i}\" OR '
    #print(str)
    print("\nThe processed keywords are here:\n",str.rstrip(' OR'))
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exit!")
