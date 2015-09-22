from twitter_setup import api
from pygeocoder import Geocoder
import pygmaps, time
'''
from datetime import datetime and date
curtime = str(datetime.now())
KEYWORD = "NHL"
filename = ("%s"+ %()
text_file = open("NHL_AP_27_15_002.txt", "w") #OPEN TEXTFILE
text_file.write("FORMAT: USERID TWEET_TIME ")
text_file.write("KEYWORD = %s AT %s \n \n" %(KEYWORD , curtime))
'''

from datetime import date

def timeIzNow():
    '''
    returns current date as a string
    '''
    now = date.today()
    full = "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.year)

    return full

fileN = "user_twetime"
name = fileN + timeIzNow() + ".txt"
myfile = open(name, 'w')
myfile.write("test text")
myfile.close()
    
