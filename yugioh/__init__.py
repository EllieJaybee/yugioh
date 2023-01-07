import requests

class Card:
    def __init__(self, q):
        for key, value in q.items():
            if key not in ("card_sets", "card_images", "card_prices"):
                if key == "def":
                    setattr(self, "def_", value)
                else:
                    setattr(self, key, value)

def __get(parameters):
    return requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php',
    params=parameters).json()['data'][0]

def get_card(query):
    if not query:
        raise ValueError
    try:
        card = __get({"id": query})
    except KeyError:
        card = __get({"fname": query})
    return Card(card)
