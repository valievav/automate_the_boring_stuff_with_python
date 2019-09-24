'''
Write a program that runs just before you wake up in the
morning and checks whether it’s raining that day. If so, have the program
text you a reminder to pack an umbrella before leaving the house.
'''
import requests, pprint

def umbrella_reminder(api_call):

    # make an api call
    api_response = requests.get(api_call)
    api_response.raise_for_status()

    # get api response
    json = api_response.json()
    pprint.pprint(json)



city_name = "Krakow"
country_code = "pl"
api_key = "f4903b072656d35aa82e06a04f1e5408"
api_call = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&units=metric&APPID={api_key}"

umbrella_reminder(api_call)

