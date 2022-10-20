# WeatherAPI
 
This simple code consists out of local server (using port 8080) and can recieve three simple get-requests: current_weather, current_info, weather_forecast.

EXAMPLE OF REQUESTS! (for more info check https://www.getpostman.com/collections/34ec17c708c8d019969d)

GET 127.0.0.1:8080/current_info/{cityname}
with this command you can get full information about current weather in chosen city, its longitude and latitude and some other.

GET 127.0.0.1:8080/current_weather/{cityname}
with this command you can get info about current weather in chosen city, like cloudiness, temperature and what it feels like

GET 127.0.0.1:8080/weather_forecast/{cityname}
with this command you can get weather forecast in chosen city.

If exception occurs, server responses with code of internal server error.