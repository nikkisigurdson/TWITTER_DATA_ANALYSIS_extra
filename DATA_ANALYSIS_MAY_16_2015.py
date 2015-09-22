#written may 16 2015
#takes in twitter txt data of "," dlm USER_ID's, and returns a
#list of the usernames.

'''
heres an idea:
since we have so much tweeter data, just do calls for the followers/following
information of like 1 user for instance, and then check to see out of the
total number of tweets we have collected (over 10,000) related to hockey
key words, how many of the total are followers/following the other person.
we can do this for all users, and then calculate the average.
'''
#CLEANNEDHOCKEY2.txt

#cleannedhockey2MM_DLM.txt
#cleannedhockey3.txt

from string import *

def clean_data1(txtfilename):
     rtxt = open( txtfilename, 'r')
     wtxt = open( "test.txt" , "w")
     
     listt = []
     for line in rtxt:
          if line != ".":
               print(line)
               listt.append(line)
               wtxt.write(line)
     '''
          listt2 = (line).split(",")
          listt.append(listt2)
     #seperate the string by a delimiter into nodes of a list
     '''
     rtxt.close()
     wtxt.close()
     return listt
     

#mylist = cleandata1("cleannedhockey4.txt")

def make_list(txtfilename):
     rtxt = open( txtfilename, 'r')
     mylist = []
     for line in rtxt:
          dlm = line.split(",")
          try:
               mylist.append(int(dlm[0]))
               #print (dlm[0])
          except:
               print("error occured with INT type. ")
     rtxt.close()
     return mylist

dataL = make_list("final_clean.txt")
print(len(dataL))


# remember that when text file data is read,
#its automatically assumed to be string data.
