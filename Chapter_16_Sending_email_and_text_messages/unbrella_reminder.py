'''
Write a program that runs just before you wake up in the
morning and checks whether it’s raining that day. If so, have the program
text you a reminder to pack an umbrella before leaving the house.
'''


import requests
import pprint
import datetime


def umbrella_reminder(api_call, number_of_timestamps):
    """
    Makes API forecast call to see if it's going to rain in the nearest hours.\n
    Returns rain forecast message, short forecast weather description and raw json data.\n
    :param api_call: valid API call link
    :param number_of_timestamps: int
    :return: rain_hours - list, forecast_weather - dict, json_data - dict
    """

    # make an api call
    api_response = requests.get(api_call)
    api_response.raise_for_status()

    # get api response
    json_data = api_response.json()

    # iterate through json and find weather for timestamps
    rain_hours = []
    forecast_weather = {}

    for timestamp in range(number_of_timestamps):
        date_js = json_data['list'][timestamp]['dt_txt']
        date = datetime.datetime.strptime(date_js, "%Y-%m-%d %H:%M:%S")
        hour = date.strftime("%H:%M")
        weather_js = json_data['list'][timestamp]['weather'][0]['main']

        # record rain hours
        if weather_js.lower() == 'rain':
            rain_hours.append(hour)

        forecast_weather.setdefault(date, weather_js)

    return rain_hours, forecast_weather, json_data


if __name__ == "__main__":
    city_name = "krakow"
    country_code = "pl"
    api_key = "f4903b072656d35aa82e06a04f1e5408"
    number_of_results = 4  # number of timestamps for 1 day (weather is provided for every 3 hours) - used 1/2 day

    api_weather_call = f"https://api.openweathermap.org/data/2.5/" \
        f"forecast?q={city_name},{country_code}&units=metric&cnt={number_of_results}&APPID={api_key}"

    rain_hours, forecast_weather, json_data = umbrella_reminder(api_weather_call, number_of_results)
    show_forecast = True
    show_json_data = False
    print_separator = '-' * 20

    # print rain forecast message
    if rain_hours:
        print(f"{print_separator}\nATTENTION!>>> Please take your UMBRELLA. "
              f"It's going to rain at around {', '.join(rain_hours)}.")
    else:
        print(f"{print_separator}\nNo rain in the forecast - have a great day!")

    # print short forecast if requested
    if show_forecast:
        print(f"{print_separator}\nShort weather forecast for the next {number_of_results*3} hours:")
        for v, k in forecast_weather.items():
            print(f"{v} - {k}")

    # print json raw data if requested
    if show_json_data:
        print(f"{print_separator}\nRaw JSON data:")
        pprint.pprint(json_data)

