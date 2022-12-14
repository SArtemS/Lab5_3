import getweatherdata
from owm_key import owm_api_key

key = owm_api_key


def test_without_key():
    assert getweatherdata.get_weather_data(
        "moscow") is None, \
        " Для получения данных необходимо задать значение для api_key "


def test_in_riga():
    assert getweatherdata.get_weather_data("Riga",
                                           api_key=key) is not None, \
        " Type of response is not none while using the key "


def test_type_of_res():
    assert type(getweatherdata.get_weather_data("Riga",
                                                api_key=key)) is dict, \
        " Type of response is not none while using the key "


def test_args_error():
    assert getweatherdata.get_weather_data(
        '') is None, \
        " There should be one positional argument: 'city' and one keyword argument 'key_arg'"


def test_pos_arg_error():
    assert getweatherdata.get_weather_data("",
                                           api_key=key) is None, \
        " There should be one positional argument: 'city' "


def test_coords_dim():
    assert len(
        getweatherdata.get_weather_data('Riga', api_key=key).get('coord')) == 2, \
        " Dimension is 2: lon and lat "


def test_temp_type():
    assert type(getweatherdata.get_weather_data('Riga', api_key=key).get(
        'feels_like')) is float, \
        " Error with type of feels_like attribute "
