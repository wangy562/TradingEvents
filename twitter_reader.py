import os, json
from dotenv import load_dotenv


class TwitterReader:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.bearer = os.getenv('TWITTER_BEARER_TOKEN')
        self.list_id = os.getenv("TWITTER_LIST_ID")
        self.tickers = {}
        self.tweet_list = []

    def generate_data(self):
        if os.path.isfile('./tickers.json') is False:
            with open('tickers.json', 'x') as f:
                json.dumps(self.tickers, f)
            f.close()

    def add_ticker(self, ticker):
        with open('tickers.json', 'x') as f:
            self.tickers = json.loads(f)
        if ticker not in self.tickers.keys():
            self.tickers[ticker] = ticker
        json.dumps(self.tickers, f)
        f.close()

    def delete_ticker(self, ticker):
        with open('tickers.json', 'x') as f:
            self.tickers = json.loads(f)
        self.ticker.pop(ticker, None)
        json.dumps(self.tickers, f) 
        f.close()

    def load_api(self):
        pass

    def get_tweets(self):
        for ticker in self.tickers:
            pass 

