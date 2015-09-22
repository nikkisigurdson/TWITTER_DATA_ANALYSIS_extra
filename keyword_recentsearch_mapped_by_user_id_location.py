# distribution_of_timezones_based_on_recent_tweet_keyword.py

from twitter_setup import api
from pygeocoder import Geocoder
import pygmaps, time

text_file = open("NHL_AP_27_15.txt", "w") #OPEN TEXTFILE

#naming system for data: keyword_monthfirst2letters_day_year.txt
# DELIMITED BY A SINGLE SPACE,ONE OBSERVATION PER LINE. 


mymap = pygmaps.maps(56.95, -98.31, 3) # initializing pygmaps
result = api.search.tweets(q = "NHL" , count = 100 ) #API CALL #1 
num = len(result['statuses'])
ids = []
print ("Total number of hits: " ,num)
for i in range(0, num):
   # print (result['statuses'][i]['user']['id_str'])
     ids.append( result['statuses'][i]['user']['id_str'] )
count = 0
address= [0,0]

for i in range(0,num):
    subquery = api.users.lookup(user_id = ids[i]) #FINDING USER INFORMATION BASED ON A RECENT TWEET 
                                                   #WITH THE KEYWORD WE ARE LOOKING FOR
    for user in subquery:
        count += 1
        print("users processing ... ", count )
        
        try:
            address = Geocoder.geocode(user['location'])
            print(address.coordinates[0] , address.coordinates[1] )

        except:
            continue # if error occurs and continue is called, the code after it will not be processed.
                     # the next iteration of the loop will begin immidiately. 

        mymap.addpoint(address.coordinates[0], address.coordinates[1])
        scoord0 = str(address.coordinates[0])
        scoord1 = str(address.coordinates[1])
        text_file.write("%s %s %s" %(ids[i], scoord0, scoord1))
        time.sleep(0.2)

 
mymap.draw('keywordsearch.html')

import webbrowser as wb
wb.open_new_tab('keywordsearch.html')
text_file.close()
#textfile naming system: USERID COORD0 COORD1


'''
is there an easier way to get the user location data, than having to take IDs
and then re run them through the api
next to-do: try switching user['location'] in the geocoder line with
result['statuses'][i]['user']['location'] to see if the results are different.
'''
