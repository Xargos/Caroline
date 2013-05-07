Caroline
========

Caroline is a program that helps with everyday tasks and questions. Using voice recognition technology, you can ask her questions like "When did Abraham Lincoln die?", "What is 2x + 7x?" or perform actions like "Search YouTube for funny cat videos". The Caroline project was forked from [Pi-Voice](https://github.com/rob-mccann/Pi-Voice).

Requirements
------------
- alsa / alsa-utils 
- python
- flac
- curl
- avconv
- [Wolfram Alpha API key](http://products.wolframalpha.com/developers/)
- An internet connection

List of Commands
----------------
This list contains some of the most useful commands. Feel free to peek at the source code and see all of the different commands in the "src/plugins" folder.

- Facebook (open Facebook, open my Facebook)
- Google (Google [keyword], translate [keyword], open Google, open Google Drive, open Google Translate)
- Wikipedia (search Wikipedia for [keyword], open Wikipedia)
- YouTube (search YouTube for [keyword], open YouTube)
- Misc. (Who are you?, Who made you?, goto [website address])

<sub><sup>The default search (with no keywords) uses [Wolfram Alpha](http://wolframalpha.com).</sup></sub>

How To Use
----------
1. Make sure you've got all the requirements installed
2. Set the Wolfram Alpha API key as an environment variable: ```export WOLFRAM_API_KEY='AAAAAA-AAAAAAAAAA'```
3. Run ```python caroline.py```
