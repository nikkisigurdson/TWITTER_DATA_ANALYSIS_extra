#module for tweet collection -> process -> output 
#april 30 2015 

def gettweets( RANGNUM1,):
    "loops through n number of request loops, output to .txt file"
for i in range(0,RANGNUM1): #number of 100-request loops
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
               time.sleep(2)
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
             
