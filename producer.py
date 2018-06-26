from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler,API
from tweepy import Stream
import json
from kafka import SimpleProducer, KafkaClient

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

class TweetListener(StreamListener):
    def __init__(self, api):
        self.api = api
        super(StreamListener, self).__init__()
        client = KafkaClient("localhost:9092")
        self.producer = SimpleProducer(client, async = True, batch_send_every_n = 1000, batch_send_every_t = 1)
    
    def on_status(self, status):
        msg = status.text.encode('utf-8')
        try:
            self.producer.send_messages(b'tweets', msg)
        except Exception as e:
            print(e)
            return False
        print("############",status.text,status.coordinates)
        return True
        
    def on_error(self, status_code):
        print("Error - kafka producer")
        return True

    def on_timeout(self):
        return True
    


        
if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    l = TweetListener(api)
    stream = Stream(auth, l)
    stream.filter(track=['#trump'])
