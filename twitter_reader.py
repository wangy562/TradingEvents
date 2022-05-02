import os, json
from dotenv import load_dotenv


class TwitterReader:

    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get('TWITTER_API_KEY')
        self.api_secret = os.environ.get('TWITTER_API_SECRET')
        self.bearer = os.environ.get('TWITTER_BEARER_TOKEN')
        self.tickers = {}

    def generate_data(self):
        if os.path.isfile('./tickers.json') is False:
            with open('tickers.json', 'x') as f:
                json.dumps(self.tickers, f)
            f.close()

    def load_tickers(self):
        pass