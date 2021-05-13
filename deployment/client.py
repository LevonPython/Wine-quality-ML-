import requests
import json
import argparse
import os.path
import sys

"""
This parser gets a json file as an input, parse it,
then send it to the specified api url via POST method
"""


# Create the parser
my_parser = argparse.ArgumentParser(prog="Json file parser",
                                    description='List the content of a folder',
                                    epilog="Enjoy the program!", prefix_chars="-")

# Add the arguments
my_parser.add_argument('file',
                       metavar='the_file',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.file


if not os.path.isfile(input_path):
    print(f'The file {input_path} specified does not exist')
    sys.exit()

url = "http://localhost:5000/predict"

# json_file_path = "preprocessing.json"
json_file_path = input_path
print(f"input_path: {input_path}")
with open(json_file_path, 'r') as j:
    contents = json.loads(j.read())
    print(contents)
    r = requests.post(url, json=contents)
    print(r.text)
