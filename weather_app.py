import requests

def get_weather(city):
    api_key = "f025766cf5e6ec985a3ddfdf9c257989"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
         # Extract weather details
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except requests.exceptions.requestexception as e:
        print('error fetching data:',e)
    except keyerror:
        print('city not found,please check the city name.')

if __name__=='__main__':
    city=input('enter city name:')
    get_weather(city)
        