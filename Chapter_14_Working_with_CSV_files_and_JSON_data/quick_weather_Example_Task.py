import json, requests, pprint, sys


def weather_results(api_call, timestamp_hour=None, get_raw_data=False):
    """
    Prints short and full data results from API JSON response.\n
    :param api_call: valid api call
    :param timestamp_hour: int, value should be divisible by 3, optional param
    :param get_raw_data: Boolean, optional param
    :return:
    """

    # solution - transforming response with json library - here to practice json library usage
    def get_json_using_json_libr(response):
        json_text = response.text  # get response in str format
        json_data = json.loads(json_text)  # transform str to json
        return json_data

    # solution using built-in json method - here to show better option (not used in program)
    def get_json_using_built_in_json_func(response):
        json_data = response.json(response)
        return json_data

    # function for retrieving 3 major data points
    def weather_brief_data(json_data, data_number):
        print(f"Date: {json_data['list'][data_number]['dt_txt']}")
        print(f"Temperature: {json_data['list'][data_number]['main']['temp']}")
        print(f"Weather: {json_data['list'][data_number]['weather'][0]['description']}\n")

    # check variables correctness
    if number_of_results > 40 or number_of_results == 0:
        print("Max number_of_results is 40 (5 days), min number_of_results is 8 (1 day).\n"
              "Please update the value accordingly.")
        sys.exit()

    if timestamp_hour % 3 != 0:
        print("Timestamp hour should be divisible by 3. Please update the value.")
        sys.exit()

    # send api call
    api_response = requests.get(api_call)
    api_response.raise_for_status()

    # get response in json format
    json_data = get_json_using_json_libr(api_response)

    # header data
    print(f"Weather in {json_data['city']['name']}, {json_data['city']['country']} "
          f"(population - {json_data['city']['population']}):\n")

    timestamp = str(timestamp_hour)+":00:00"

    # iterating through json datetime and printing short weather outlook
    for data_number in range(number_of_results):
        date_str = json_data['list'][data_number]['dt_txt']
        if timestamp_hour:
            if date_str.endswith(timestamp):
                weather_brief_data(json_data, data_number)
        else:
            weather_brief_data(json_data, data_number)

    # print complete raw data if requested
    if get_raw_data:
        print("-"*8+"\nRaw data:")
        pprint.pprint(json_data)


city_name = "Krakow"
country_code = "pl"
api_key = "******"

number_of_days = 5
number_of_results = 8*number_of_days  # 8 is a number of timestamps returned for 1 day (weather is provided for every 3 hours)
hour_to_retrieve = 9

weather_api_call = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&units=metric&cnt={number_of_results}&APPID={api_key}"
get_raw_data_flag = False

weather_results(weather_api_call, hour_to_retrieve, get_raw_data_flag)

