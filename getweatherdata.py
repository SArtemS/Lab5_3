import json
import requests


def get_weather_data(place, api_key=None):
    if api_key:
        with requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
        ) as f:
            res = f.text
            res_obj = json.loads(res)
        if 'Nothing to geocode' in res_obj.values(): return None
        res_dict = {}
        utc_div = 3600
        Celsius_diff = 273.15
        tzh = res_obj["timezone"] // utc_div
        tzm = int(abs(60 * (res_obj["timezone"] / utc_div % 1)))
        res_dict.setdefault("name", f"{place}")
        res_dict.setdefault("country", res_obj["sys"]["country"])
        res_dict.setdefault("coord", res_obj["coord"])
        if tzh >= 0:
            res_dict.setdefault("timezone", f"UTC+{tzh:02}:{tzm:02}")
        else:
            res_dict.setdefault("timezone", f"UTC-{-tzh:02}:{tzm:02}")
        res_dict.setdefault("feels_like", float(format(res_obj["main"]["feels_like"] - Celsius_diff, '.2f')))

        with open('data.json', 'w') as f:
            json.dump(res_dict, f, ensure_ascii=False, indent=4)

        return res_dict
    
    
if __name__ == "__main__":
    pass
