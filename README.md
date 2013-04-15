Caroline
========

Caroline is a program that helps with everyday tasks and questions. Using voice recognition technology, you can ask her questions like "When did Abraham Lincoln die?", "What is 2x + 7x" or even "Google cat videos". The Caroline project was forked from [Pi-Voice](https://github.com/rob-mccann/Pi-Voice).

Requirements
------------
- alsa / alsa-utils 
- python
- flac
- curl
- avconv
- [Wolfram Alpha API key](http://products.wolframalpha.com/developers/)
- An internet connection

Usage
-----
1. Make sure you've got all the requirements installed
2. Set the Wolfram Alpha API key as an environment variable ```export WOLFRAM_API_KEY='AAAAAA-AAAAAAAAAA'```
3. Make sure src/listen.sh has execute privileges, or type ```chmod a+x src/listen.sh```
3. Run ```./listen.sh```

How It Works
------------
When you run the command, Caroline listens to the microphone for 6 seconds. She then sends the user's voice to Google to be converted into text. Using an array of websites and services, she returns with a string of text. Finally, she sends the response to Google's Text-To-Speech engine which then reads the response out to the user.