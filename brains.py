#!/usr/bin/python
# -*- coding: utf-8 -*-
import wolframalpha
import os
import sys
import json
import webbrowser

# Read the input from Google's speech recognition
jsonstr = sys.stdin.readlines()

if len(jsonstr) == 0:
    print "I didn't quite understand what you said."
    sys.exit(0)

jsonstr = jsonstr[0]
phrase = json.loads(jsonstr)
phrase = phrase['hypotheses'][0]['utterance']

# output to stderr for debug purposes
sys.stderr.write(phrase + "\n")

# strip "computer" from beginning of phrase
if phrase.startswith("computer "):
    phrase = phrase[9:]

if phrase.lower().startswith("google "):
    phrase = phrase[7:]
    url = "https://encrypted.google.com/search?hl-en&q=" + phrase
    webbrowser.open(url)
    print "Googling " + phrase
else:
    # grab the user's api key
    key = os.environ.get('WOLFRAM_API_KEY')

    if not key:
        print "I can't contact the knowledge base without an API key. Set one in an environment variable."
        sys.exit(0)

    client = wolframalpha.Client(key)

    # ask wolfram alpha for any info based on the query
    res = client.query(phrase)

    try:
        if len(res.pods) == 0:
            raise StopIteration()

        for pod in res.results:
            if hasattr(pod.text, "encode"):
                # festival tts didn't recognise the utf8 degrees sign so we convert it to words
                # there's probably more we need to add here
                # convert to ascii too to prevent moans
                print pod.text.replace(u"°", ' degrees ').encode('ascii', 'ignore')
                sys.exit(0)
            else:
                break

        print "I found a result but could not read it out to you. It could be a map, image or table."
    except StopIteration:
        print "I couldn't find any results for the query, '" + phrase + "'"