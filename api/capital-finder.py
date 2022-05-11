from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if 'country' in dic:
            country = dic['country']
            url = f'https://restcountries.com/v3.1/name/{country}'
            res = requests.get(url)
            data = res.json()
            capital = data[0]['capital'][0]
            message = f'The capital of {country.title()} is {capital.title()}.'
        elif 'capital' in dic:
            capital = dic['capital']
            url = f'https://restcountries.com/v3.1/capital/{capital}'
            res = requests.get(url).json()
            data = res.json()
            country = res[0]['name']['common']
            message = f'{capital.title()} is the capital of {country.title()}.'
        else:
            message = "Please enter a country or a capital."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())
        return
