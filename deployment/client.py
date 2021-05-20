import requests
import json
import argparse
import os.path
import sys
import pandas as pd
from data_wrangler import DataWrangler
import socket


def json_parser(url):

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


    # json_file_path = "preprocessing.json"
    json_file_path = input_path
    print(f"input_path: {input_path}")
    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
        print(contents)
        data = contents['data']
        df = pd.DataFrame.from_dict(data, orient='columns')
        print("---Raw data------")
        print(df.head(20))
        df.to_csv('data/instance_raw.csv')
        df = DataWrangler.lst_of_dataframes(DataWrangler.oversampling_data(DataWrangler.data_correcting(df)))
        print("---Wranglered data------")
        print(df.head(20))
        df.to_csv('data/instance_wrangler.csv')

        # convert wranglered data to json format and POST to API
        json_file = json.loads(df.to_json(orient="split"))
        print(json_file)
        r = requests.post(url, json=json_file)
        print(r.text)


if __name__ == "__main__":
    # api_url = "http://localhost:5000/predict"
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Ip address: {local_ip}")
    api_url = f"http://{local_ip}:5000/predict"
    json_parser(api_url)
