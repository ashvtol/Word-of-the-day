# Word-of-the-day
Get "Word of the day" from wordsmith.org directly into your terminal.
Also, the "Thought for the day" from brainyquote.com is now included. 


### Dependencies
1. Python 3.5 or greater
2. feedparser module
4. bs4
5. BeautifulSoup4

```
To get the feedparser module
1. In terminal enter : sudo pip3 install feedparser
   If you don't have pip3 you can use pip as well but then 
   make sure it gets installed for python3 and not any other
   version
2. Or to install directly to python3 use pip3
3. If you don't have pip3 use this <a=href="https://bootstrap.pypa.io/get-pip.py">link</a=> to download get-pip.py
4. Simply run python3 get-pip.py.

```
## Usage
```
1. Navigate to the folder
2. Open your terminal
3. Hit "make" (assuming that the make utility comes by default on OSX)


If not, then just run
1. python3 word_parser.py
2. To get the past recorded words 
	python3 word_parser some_integer
   Here some_integer refers to the number of recorded words you want to
   display.
```

## Output
<img src="https://github.com/ashvtol/Word-of-the-day/blob/master/img/screen.png" width="595px"></img>


## To Run Direclty from Terminal
```
1. Navigate to the folder in the terminal.
2. Create a file, for simplicity call it word.
	using: touch word
   Then write the following into it.
3. vim touch
4. #!/bin/bash
5. cd /Users/YOUR_USER_NAME/_PATH_/wordoftheday
6. python3 word_parser.py
7. save it and then make it executable:
	chmod u+x word	
8. Set the path in the bash_profile
	cd ~/
	vim ./bash_profile
	export PATH=$PATH:/Users/YOUR_USER_NAME/_PATH_/wordoftheday
9. save it.
10. Reopen the terminal and type
11. word
12. BAM!
```
