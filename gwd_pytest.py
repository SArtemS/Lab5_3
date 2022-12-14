import getweatherdata
import pytest 
from owm_key import owm_api_key


key = owm_api_key
inp_params_1 = "city, api_key, expected_country"
exp_params_countries = [("Chicago", key, 'US'),
                        ("Saint Petersburg", key, 'RU'), ("Dakka", key, 'BD'),
                        ("Minsk", key, 'BY'), ("Kioto", key, 'JP'),
                        ("Anchorage", key, 'US'), ("Havana", key, 'CU')]


@pytest.mark.parametrize(inp_params_1, exp_params_countries)
def test_countries(city, api_key, expected_country):
    assert getweatherdata.get_weather_data(city, api_key=key).get('country',
        'NoValue') == expected_country, \
        " Error with country code "
        

def UTC_format(timezone_name):
    import pytz
    from datetime import datetime
    return str(datetime.now(pytz.timezone(timezone_name)))[-6:]


inp_params_2 = "city, api_key, expected_time"
exp_params_timezones = [("Chicago", key, UTC_format('US/Central')),
                        ("Saint Petersburg", key, UTC_format('Europe/Moscow')),
                        ("Dakka", key, UTC_format('Asia/Dhaka')), 
                        ("Minsk", key, UTC_format('Europe/Moscow')),
                        ("Kioto", key, UTC_format('Japan')), 
                        ("Anchorage", key, UTC_format('US/Alaska')),
                        ("Havana", key, UTC_format('Cuba'))]


@pytest.mark.parametrize(inp_params_2, exp_params_timezones)
def test_utc_time(city, api_key, expected_time):
    assert getweatherdata.get_weather_data(city, api_key=key).get('timezone',
         'NoValue') == "UTC" + expected_time, \
        " Error with timezone "