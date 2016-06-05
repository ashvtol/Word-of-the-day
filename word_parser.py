import feedparser
import time
import socket
import sys

word = "";
meaning = "";
REMOTE_SERVER = "www.google.com"

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   I = '\t\033[1m'

###################################################################
############################ Word of the day ######################
def wod():
    global word;
    global meaning;
    raw_feed = feedparser.parse("https://wordsmith.org/awad/rss1.xml")
    word = str(raw_feed.entries[0]['title'])
    word = word.capitalize();
    meaning = str(raw_feed.entries[0]['summary_detail'].value)
    localtime = time.asctime( time.localtime(time.time()))
    print(color.PURPLE + "------------------------------------------------------------------------------\n" + color.END)
    print(localtime)
    print(color.BOLD + "Word    : "  + color.YELLOW + word + color.END )
    print(color.BOLD + "Meaning : " + color.RED +meaning+ color.END)
    page = str(raw_feed.entries[0]['link'])
    print(color.BOLD + "Usage   : " + color.END + color.UNDERLINE + page + color.END + " (use ⌘ + doubleclick to open)\n")

####################################################################
############################## Store Word ##########################
#Load Existing Words
####################
def load_and_store():
    global word;
    global meaning;
    with open('./word_log',"r", encoding="utf-8") as f:
        wlog = {};
        for line in f:
            line = line.strip();
            line = line.split(":");
            #print(line[0], line[1]);
            if(line!=""):
                line[0] = line[0].strip();
                wlog.update({line[0]:line[1]})
    f.close();
    
    ###############
    #Remap Process

    try:
        wlog[word]
        #print(wlog[word])
    except KeyError:
        print(color.BOLD + "\nNew word " + color.END + color.RED+ "recorded" + color.END);
        with open('./word_log',"a") as f:
            f.write((word + " : " + meaning+"\n"));
        f.close();
        print("Congrats! You learned a new word today");
        print("To view recorded words open " + color.BOLD + "word_log\n" + color.END)
    
######################## Connection Status #######################
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

x  = is_connected()
if(x):
	print(color.BOLD + color.RED)
	print(" _______________________ AZ ________________________ ")
	print("|                                                   |")
	print("|         Created by Ashish on 05/06/16.            |")
	print("|   Copyright © 2016 Ashish. All rights reserved.   |")
	print("|___________________________________________________|") 
	print(color.END)
if(x):
    print("Internet : "+ color.GREEN + "connected" + color.END);
    print(color.BOLD + color.UNDERLINE + "Word of the day" + color.END)
    wod();
    load_and_store();
else:
    print("Internet: " + color.RED +"disconnected" + color.END +"\n " + color.UNDERLINE + "Check connection and try again " + color.END);
print(color.PURPLE + "------------------------------------------------------------------------------\n" + color.END)