from zen_quotes.config import Config
import requests, json

class Quotes():

    def __init__(self):
        self._url = None
    
    def get_lang(self, lang=None):
        if lang is None:
            self._url = Config.get('URL', 'api_quotes')
        else:
            self._url = Config.get('URL', 'api_quotes') + f'/{lang}'

    def get_quotes(self, lang = None, quote = None):
        """
        Busca na API Challenge Quotes, as citações 'Zen of Python'.
        """
        self.get_lang(lang)

        if quote is not None:
            response = requests.get(self._url + f"/{quote}")
        else:
            response = requests.get(self._url)

        return response.json()

if __name__ == "__main__":
    q = Quotes()
    # print(q.get_quotes(lang='pt', quote=1))
    print(q.get_quotes())