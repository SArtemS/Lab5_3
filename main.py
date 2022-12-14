from owm_key import owm_api_key
from getweatherdata import get_weather_data

key = owm_api_key

if __name__ == '__main__':
    print(get_weather_data('New York', api_key=owm_api_key))
    