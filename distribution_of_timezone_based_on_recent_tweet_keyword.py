# distribution_of_timezones_based_on_recent_tweet_keyword.py

from twitter_setup import api
from pygeocoder import Geocoder
import pygmaps, time


mymap = pygmaps.maps(56.95, -98.31, 7)
result = api.search.tweets(q = "kathneil" , count = 100 )
num = len(result['statuses'])
ids = []
for i in range(0, 100):
   # print (result['statuses'][i]['user']['id_str'])
     ids.append( result['statuses'][i]['user']['id_str'] )
count = 0

for i in range(0,100):
    subquery = api.users.lookup(user_id = ids[i])
    for user in subquery:
        count += 1
        print("users processing ... ", count )
        try:
            address = Geocoder.geocode(user['location'])
        except:
            continue
        mymap.addpoint(address.coordinates[0], address.coordinates[1])
        time.sleep(0.2)

 
mymap.draw('twitter.geocoder.html')
