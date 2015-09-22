#written by nikki sigurdson 
from twitter_setup import api
from time import strftime, gmtime
import time, math
from datetime import datetime
KEYWORD = "imthebest"

filenametime = str( math.ceil(time.time()))
timenow = strftime("%X")
timeatstart=timenow
name = "TEXT_" + KEYWORD + "__" + filenametime + ".txt"
text_file = open(name, 'w')
filenametime = str( math.ceil(time.time()))

text_file.write("FORMAT: USERID [SPACE] TWEET_TEXT \n")
text_file.write("KEYWORD = '%s' \n %s \n \n" %( KEYWORD ,strftime("%a, %d %b %Y %X +0000", gmtime()) ))
tweetlist= []
#naming system for data: keyword_monthfirst2letters_day_year.txt
# DELIMITED BY A SINGLE SPACE,ONE OBSERVATION PER LINE.

tweetcounter = 0
uniquecounter = 0

for i in range(0,1): #number of 100-request loops
    print("main iteration number ", i)
    result = api.search.tweets(q = KEYWORD , count = 100) #API CALL
    #result is a twitter dict type, or converted JSON
    count = len(result['statuses'])
    for i in range(0,count):
        tweetcounter += 1
        try:
          #for key, value in result['statuses'][i].items() :
          #   print(key, "  " , value)
          if (result['statuses'][i]['text']) in tweetlist:
               print("[ duplicate tweet detected. (error = 0) ] ")
               time.sleep(2.5)
               continue
          for tweet in tweetlist:
            if tweet[0:15] == (result['statuses'][i]['text'][0:15]):
               print("[ duplicate tweet detected. (error = 1) ] ")
               time.sleep(2.5)
               continue
          else:
            print(tweetcounter , result['statuses'][i]['text'])
            text_file.write(" %s , %s \n " %(result['statuses'][i]['user']['id_str'], result['statuses'][i]['text'])  )
            #add this tweet to the master tweet list
            tweetlist.append( result['statuses'][i]['text'] )
            uniquecounter += 1
            time.sleep(2.5)
            
        except:
             print("[ an exception occured. (level = 2)]")
             continue
             

text_file.close()
print("TEXT file successfully closed. ")

timeatend = strftime("%X")

print ("started at %s. Ended at %s."  %(timeatstart,timeatend))
print("observed %i total tweets, %i unique tweets" %(tweetcounter, uniquecounter))
