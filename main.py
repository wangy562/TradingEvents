import os
import sys
import argparse
from twitter_reader import TwitterReader


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Aggregates major trading events from various Twitter accounts.")
    parser.add_argument("--add-ticker", "-a", nargs="+",
                        help="Add the tickers")
    parser.add_argument("--delete-ticker", "-d", nargs="+",
                        help="Delete the tickers beginning with $")
    args = parser.parse_args()
    twitter_reader = TwitterReader()
    twitter_reader.generate_data()
    if twitter_reader.load_api() is True:
        twitter_reader.get_tweets()

        for t in args.a:
            twitter_reader.add_ticker(t)
