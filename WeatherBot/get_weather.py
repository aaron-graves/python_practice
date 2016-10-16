#uses the Weather Underground API to get weather conditions.
#if used be sure to attribute WU

from urllib.request import urlopen
import json

#get state and city for url
#i have these hard coded in the version I use, so the script can run on it's own
state = input("Enter state: ")
city = input("Enter city: ")

#get current conditions
def get_current(state,city):
    city = replace_spaces(city);
    f = urlopen("http://api.wunderground.com/api/8fd48eef21c613b9/conditions/q/"+str(state)+"/"+str(city)+".json")
    json_string = f.read()
    parsed_json = json.loads(json_string)
    city = parsed_json['current_observation']["display_location"]['city']
    temp_f = parsed_json['current_observation']['temp_f']
    print("Current temperature: " + str(temp_f) + "F in " + str(city)+ ".")
    f.close()
    return temp_f

#get forecast
def get_forecast(state,city):
    city = replace_spaces(city);
    f = urlopen("http://api.wunderground.com/api/8fd48eef21c613b9/forecast/q/"+str(state)+"/"+str(city)+".json")
    json_string = f.read()
    parsed_json = json.loads(json_string)
    forecast = parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext']
    print("Forecast: "+forecast)
    f.close()
    return forecast

#replaces blank spaces with underscores (used for two word cities)
def replace_spaces(city):
    city = city.replace(" ","_")
    return city

#run program
forecast = get_forecast(state,city)
c_temp = get_current(state,city)