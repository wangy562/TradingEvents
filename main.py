import os, sys, argparse
from twitter_reader import TwitterReader


def build_parser():
    parser = argparse.ArgumentParser(description="Aggregates major trading events from various Twitter accounts.")
    parser.add_argument("--add-ticker", "-a", nargs="+", help="Add the tickers beginning with $")
    parser.add_argument("--delete-ticker", "-d", nargs="+", help="Delete the tickers beginning with $")
    return parser


if __name__ == "__main__":
   parser = build_parser()
   args = parser.parse_args()
   twitter_reader = TwitterReader()
   twitter_reader.generate_data()
