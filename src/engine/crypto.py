import requests
import json


# Gets the current price of a cryptocurrency
def get_cryptocurrency_price(cryptocurrency):
    """
    Gets the current price of a cryptocurrency
    :param cryptocurrency: cryptocurrency to get the price of
    :return: current price of the cryptocurrency
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=" + cryptocurrency + "&vs_currencies=usd"
    response = requests.get(url)
    response_json = json.loads(response.text)
    return response_json[cryptocurrency]["usd"]
