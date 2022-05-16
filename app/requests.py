import requests
from .models import Quotes


url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    '''Function that consumes an API and returns '''
    response = requests.get(url).json()

    random_quote = Quotes(response.get("author"), response.get("quote"))
    return random_quote


