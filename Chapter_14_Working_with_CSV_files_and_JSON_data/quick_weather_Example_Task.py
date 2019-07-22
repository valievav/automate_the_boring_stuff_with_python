import json, requests, pprint


def weather_results(api_call):
    """
    Prints result of API call in JSON format.\n
    :param api_call: valid api call
    :return:
    """

    # solution - transforming response with json library - here to practice json library usage
    def get_json_using_json_libr(response):
        json_text = response.text  # get response in str format
        json_data = json.loads(json_text)  # transform str to json
        return json_data

    # solution using built-in json method - here to show better option
    def get_json_using_built_in_json_func(response):
        json_data = response.json(response)
        return json_data

    # send api call
    api_response = requests.get(api_call)
    api_response.raise_for_status()

    # get response in json format
    json_data = get_json_using_json_libr(api_response)

    # print raw data
    print("Raw data:")
    pprint.pprint(json_data)


city_name = "Hong Kong"
country_code = "hk"
api_key = "f4903b072656d35aa82e06a04f1e5408"
number_of_results = 5
api_call = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&units=metric&cnt={number_of_results}&APPID={api_key}"

weather_results(api_call)

