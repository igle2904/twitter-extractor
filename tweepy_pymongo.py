import tweepy
import json
from pymongo import MongoClient
 
client = MongoClient('localhost', 27017)
db = client.aid_venezuela

class StreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        print('Error: ' + repr(status_code))
        return False # Cerramos el stream y se para la búsqueda de tweets
 
    def on_data(self, data):
        datajson = json.loads(data)
        db.cooltweets.insert(datajson)

    def on_timeout(self):
        print('Timeout...')
        return True # Sigue el stream conectado buscando tweets
 

CONSUMER_KEY =''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Autentificación
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
streamer.filter(track=['#venezuela','#aidvenezuela', '#conciertovenezuela', '#ayudahumanitaria'])


