import feedparser
import subprocess
import math
import time
import random
import socket
import sys
import os
import requests
from bs4 import BeautifulSoup

previous_stat = 0;

word = "";
meaning = "";
REMOTE_SERVER = "www.google.com"
thought = "";
weektheme = ""
word_mean = ""
use = ""
raw_thought = "";
raw_feed = "";
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

###################################################################
########################## Thought for the day ####################
def tof():
  print(color.GREEN +"------------------------------------------------------------------------------"+ color.END)
  global thought;
  global raw_thought;
  print(color.UNDERLINE + color.BOLD +"Thought for the day\n" + color.END)
  #print(raw_thought);
  iterator = random.randrange(0,4,2);
  author  = str(raw_thought.entries[iterator]['title'])
  thought = str(raw_thought.entries[iterator]['summary_detail'].value)
  length = (len(thought))
  if(length > 90):
    length = length%90;
  tabs = math.ceil(length/9);
  print(color.BOLD+thought+color.END);
  for i in range(1,tabs):
    print("\t",end='');
  print("~ " + color.YELLOW +author + color.END)
  print(color.GREEN +"______________________________________________________________________________\n\n"+ color.END)
###################################################################
############################ Word of the day ######################
def wod():
    global word;
    global meaning;
    global raw_feed;
    word = str(raw_feed.entries[0]['title'])
    word = word.capitalize();
    meaning = str(raw_feed.entries[0]['summary_detail'].value)
    length = len(meaning)
 	######################################################################
    ########################## This week's theme #########################
    global weektheme;
    theme =  str(soup.get_text());
    start = theme.find("This week’s theme")
    i = start+18;
    while(theme[i]!="\n"):
  	  weektheme = weektheme+theme[i];i = i+1;
    weektheme = weektheme + "\n";
    print(weektheme);
    # if(eme[start+17]=="\n"): 17 = "The week's theme"
    # 	print("True\n");
    #print(length)
    #######################################################################
    #######################################################################
    #######################################################################
    ################## Meaning ##############################################
    global word_mean;
    #link = "http://wordsmith.org/words/today.html";
    #html = requests.get(link).text;
    #soup = BeautifulSoup(html, 'lxml')
    #eme =  str(soup.get_text());
    #print(eme)
    start = theme.find("MEANING:")
    # if(eme[start+9]=="\n"):
    # 	print("True\n");
    i = start+10;
    while(theme[i]!="\n"):
    	word_mean = word_mean + theme[i];
    	if(theme[i]=="\n"):
    		#use  = use + "True";
    		for z in range(1,11):
    			word_mean = word_mean + " ";
    	i = i+1;
    word_mean = word_mean + "\n";
    #print(word_mean);
    ############################################# USAGE OF THE WORD ########
    global use;
    #link = "http://wordsmith.org/words/today.html";
    #html = requests.get(link).text;
    #soup = BeautifulSoup(html, 'lxml')
    #eme =  str(soup.get_text());
    #print(eme)
    start = theme.find("USAGE:")
    # if(eme[start+9]=="\n"):
    # 	print("True\n");
    i = start+8;
    while(theme[i]!="”"):
    	use = use + theme[i];
    	if(theme[i]=="\n"):
    		#use  = use + "True";
    		for z in range(1,11):
    			use = use + " ";
    	i = i+1;
    use = use + "”\n";
    #print(word_mean);
    #######################################################################
    #######################################################################
    #######################################################################

    print(color.PURPLE + "------------------------------------------------------------------------------" + color.END)
    print(color.BOLD + color.UNDERLINE + "Word of the day\n" + color.END)
    print(color.BOLD + "Theme   : "  + color.YELLOW + weektheme + color.END ,end='')
    print(color.BOLD + "Word    : "  + color.YELLOW + word + color.END )
    # print(color.BOLD + "Meaning : " + color.RED ,end='')
    # for i in range(0,len(meaning)):
    #   if(meaning[i]==';'):
    #     print("\n         ",sep='',end='');
    #   else:
    #     print(meaning[i],sep='',end='')
    # print(color.END);
    page = str(raw_feed.entries[0]['link'])
    print(color.BOLD + "Meaning : " + color.END + color.RED + word_mean + color.END,end='')
    print(color.BOLD + "Usage   : " + color.END + use ,end='')
    print(color.BOLD + "Link    : " + color.END + color.UNDERLINE + page + color.END)
    #print(color.PURPLE + "------------------------------------------------------------------------------" + color.END)

# def theme():
# 	 # uf = urllib.request.urlopen("http://wordsmith.org/words/today.html")
# 	 # html = uf.read()
# 	 # raw_feed = feedparser.parse("http://wordsmith.org/words/today.html")
# 	 # theme = str(raw_feed);
# 	 # print(html);
#  global word_mean;
#  link = "http://wordsmith.org/words/today.html";
#  html = requests.get(link).text;
#  soup = BeautifulSoup(html, 'lxml')
#  eme =  str(soup.get_text());
#  #print(eme)
#  start = eme.find("MEANING:")
#  # if(eme[start+9]=="\n"):
#  # 	print("True\n");
#  i = start+10;
#  while(eme[i]!="\n"):
#  	word_mean = word_mean + eme[i];
#  	i = i+1;
#  word_mean = word_mean + "\n";
#  print(word_mean);
# 	 # for i in range (start+18,start+17+20):
# 	 # 	print(eme[i],end='');


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
        print(color.BOLD + "New word " + color.END + color.RED+ "recorded" + color.END);
        with open('./word_log',"a") as f:
            f.write((word + " : " + meaning+"\n"));
        f.close();
        print("Congrats! You learned a new word today");
        print("To view recorded words open " + color.BOLD + "word_log\n" + color.END)
        print("Or run this program with an argument for ex.\n" + color.BOLD + "python3 word_parser.py 6" + color.END)
        print( "Here "+ color.BOLD + "6 " + color.END + "is the number of past recorded words.")
    print(color.PURPLE + "______________________________________________________________________________" + color.END)


##################################################################
########################### Previous Word ########################
def pword(index):
	
	print("Previous "+ color.RED + color.BOLD + index + color.END +" Words" + color.BOLD);
	p  = subprocess.Popen('tail -' + index + ' word_log', stdout=subprocess.PIPE, shell=True)
	print(p.stdout.read().decode() + color.END)

    
######################## Connection Status #######################
def is_connected():
  # try:
  #   # see if we can resolve the host name -- tells us if there is
  #   # a DNS listening
  #   host = socket.gethostbyname(REMOTE_SERVER)
  #   # connect to the host -- tells us if the host is actually
  #   # reachable
  #   s = socket.create_connection((host, 80), 2)
  #   return True
  # except:
  #    pass
  # return False
  hostname = "8.8.8.8"
  response = os.system("ping -c 1 -t 1 " + hostname +  " > /dev/null");
  if(response==0):
  	return 1;
  else:
  	return 0;


x  = is_connected()
# if(x):
# 	theme();
if(x):
	print(color.BOLD + color.RED)
	print(" _______________________ AZ ________________________ ")
	print("|                                                   |")
	print("|         Created by Ashish on 05/06/16.            |")
	print("|   Copyright © 2016 Ashish. All rights reserved.   |")
	print("|___________________________________________________|") 
	print(color.END);
	print("Internet : "+ color.GREEN + "connected" + color.END);
	raw_feed = feedparser.parse("https://wordsmith.org/awad/rss1.xml");
	raw_thought = feedparser.parse("http://feeds.feedburner.com/brainyquote/QUOTEBR");
	link = "http://wordsmith.org/words/today.html";
	html = requests.get(link).text;
	soup = BeautifulSoup(html, 'lxml')
	localtime = time.asctime( time.localtime(time.time()));
	print("Today : ",end = '');
	print(color.BOLD + localtime + color.END);
	wod();
	try:
		previous_stat = sys.argv[1];
	except IndexError:
		previous_stat = 0;

	if(previous_stat != 0):
		pword(previous_stat);
		load_and_store();
	tof();

else:
	print("Internet: " + color.RED +"disconnected" + color.END +"\n " + color.UNDERLINE + "Check connection and try again " + color.END);
	print(color.PURPLE + "------------------------------------------------------------------------------\n" + color.END)

