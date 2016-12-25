import time, os, sqlite3, tweepy, json, re, csv
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

# SQLite connection
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db = sqlite3.connect(os.path.join(BASE_DIR, 'database.db'))
# Migrations
db.execute('''
    create table if not exists tweets(
        id int primary key not null,
        text
        created_at datetime not null
    )
''')

# Twitter Auth
consumer_key = '7VbJcjcPoPEbceUaUqHYFFSgR'
consumer_secret = 'F5daUy86T1Km53gVxQGA1C483FWb0y6vlv7Idg5nCJwg8qikJJ'

token = '807082314-9jeWrxnlZkSNX6mLzxJik53cBJzfDEJLyGWvswmQ'
secret = '4ld3XBHt1YLalQIFJ4N5GpVv591cvSFiG14sLniXmpN0g'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(token,secret)

api=tweepy.API(auth)
       
class TweepyStreamListener(tweepy.StreamListener):
    
    def on_data(self, raw):
            with open('data.json','a') as f:
                f.write("%s\n" % raw)
            return True
        except Exception as err:
            return err
 
    def on_error(self, status):
        print(status)
        return True 


streamListener = TweepyStreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track = ['PP','pp','Rajoy'], languages=['es'])




