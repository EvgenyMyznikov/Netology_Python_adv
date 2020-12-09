import requests
import json
import os

URL = "https://en.wikipedia.org/w/api.php"


class CountryIter:

    def __init__(self, file_name):
        self.counter = 0
        with open(file_name, 'r', encoding='utf-8') as f:
            self.data = [country_name['name']['common'] for country_name in json.loads(f.read())]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.data):
            country = self.data[self.counter]
            PARAMS = {
                "action": "opensearch",
                "search": country,
                "limit": 1,
                "format": "json"
            }
            response = requests.get(url=URL, params=PARAMS)
            country_url = response.json()[3][0]
            country_info = f'{self.counter + 1}.{country} - {country_url}\n'
            with open(path, 'a', encoding='utf-8') as f:
                f.write(country_info)
            self.counter += 1
            return country_info
        else:
            raise StopIteration


if __name__ == '__main__':
    path = os.path.abspath('countries.txt')
    country_iter = CountryIter('countries.json')
    for elem in country_iter:
        print(elem, end='')
