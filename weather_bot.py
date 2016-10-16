#import libraries, credentials, and variables form twitter_weather
import tweepy, time
from credentials import *
from twitter_weather import *

#variable initialization
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#updates status with current temperature, forecast, and WU image
def weather_update():
    forecast = get_forecast(state,city)
    c_temp = get_current(state,city)
    status = "Current temp: "+str(c_temp)+"F  ||  Forecast: "+str(forecast)
    api.update_with_media("wundergroundLogo_4c_horz.jpg",status)
