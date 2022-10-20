import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import requests

APPID = ""  # <-- Put your OpenWeatherMap appid here!
URL_BASE = "https://api.openweathermap.org/data/2.5/"


def current_weather(q: str = "London", appid: str = APPID) -> dict:
    return requests.get(URL_BASE + "weather", params=locals()).json()


def weather_forecast(q: str = "London", appid: str = APPID) -> dict:
    return requests.get(URL_BASE + "forecast", params=locals()).json()


def weather_onecall(lat: float = 55.68, lon: float = 12.57, appid: str = APPID) -> dict:
    return requests.get(URL_BASE + "onecall", params=locals()).json()


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class HttpGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            _request = self.requestline.split('/')
            _request = [word.split(' ') for word in _request]
            _req = []
            for dict in _request:
                for word in dict:
                    _req.append(word)
            _request = _req
            print(_request)
            if 'current_info' in _request:
                i = _request.index('current_info')
                city = _request[i + 1]
                data = json.dumps(current_weather(city))
                self.wfile.write(data.encode())
                self.send_response(200)
            elif 'weather_forecast' in _request:
                i = _request.index('weather_forecast')
                city = _request[i + 1]
                data = json.dumps(weather_forecast(city))
                self.wfile.write(data.encode())
                self.send_response(200)
            elif 'current_weather' in _request:
                i = _request.index('current_weather')
                city = _request[i + 1]
                _data = current_weather(city)
                data = {'weather': _data['main']}
                data = json.dumps(data)
                self.wfile.write(data.encode())
                self.send_response(200)
            else:
                self.send_response(404)
        except Exception:
            self.send_response(501)


run(handler_class=HttpGetHandler)
