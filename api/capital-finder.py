from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if 'country' in dic:
            query = dic['country']
            url = f'https://restcountries.com/v3.1/name/{query}'
            res = requests.get(url)
            data = res.json()
            capital = data[0]['capital'][0]
            message = f'The capital of {query.title()} is {capital.title()}.'

        else:
            message = "Please enter a country."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())
        return
