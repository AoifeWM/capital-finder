from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

# https://restcountries.com/v3.1/name/{name}
# https://restcountries.com/v3.1/capital/{capital}


class handler(BaseHTTPRequestHandler):
    # http://localhost:3000/api/define?word=python
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            data = r.json()
            capital = str(data[0]["name"][0])
            message = "The capital of {count} is {cap}.".format(count=dic["country"], cap=capital)
        elif "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            country = str(data[0]["name"]["common"])
            message = "{cap} is the capital of {count}.".format(cap=dic["capital"], count=country)
        else:
            message = "No country found"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
    