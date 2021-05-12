"""This is dedicated for training related staff."""
from argparse import ArgumentParser

import pandas as pd
from src.pipelines import run_training


def parse_args(*argument_array):
    parser = ArgumentParser()
    parser.add_argument(
        '--data-path',
        required=True,
        help='The path to save the pipeline'
    )
    parser.add_argument(
        '--label-path',
        required=True,
        help='The path to save the pipeline'
    )
    parser.add_argument(
        '--pipe-path',
        required=True,
        help='The path to save the pipeline'
    )
    return parser.parse_args(*argument_array)


def main():
    args = parse_args()
    run_training(pd.read_csv(args.data_path), pd.read_csv(args.labels_path), args.pipe_path)


if __name__ == "__main__":
    main()
