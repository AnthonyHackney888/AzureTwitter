import pyowm
import tweepy

auto_message_greet = 'AUTO TWEET: '
consumer_key = '*'
consumer_secret = '*'
access_token = '*'
acces_token_secret = '*'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_token_secret)

def weatherObserver():
    openWeatherApi = '37fb783435120c007185356fb28e652a'
    owm = pyowm.OWM(openWeatherApi)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Grand Rapids,US')
    w = observation.weather
    a=w.temperature('fahrenheit').get("temp")
    b=w.temperature('fahrenheit').get("temp_max")
    c=w.temperature('fahrenheit').get("temp_min")
    d=w.temperature('fahrenheit').get("feels_like")
    e=("Current temp: "+str(a)+"f Max temp: "+str(b)+"f Min temp: "+str(c)+"f feels like: "+str(d)+"f")
    return(e)
def main():
    api = tweepy.API(auth)
    api.update_status(auto_message_greet + weatherObserver())

if __name__ =='__main__':
    main()