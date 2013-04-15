import sys
import webbrowser
import globalvars

def google(letters):
    url = "https://encrypted.google.com/search?hl-en&q=" + phrase[letters:]
    webbrowser.open(url)
    print "Googling \"" + phrase + "\""
    sys.exit(0)

def main():
    
    if globalvars.phrase.lower().startswith("google "):
        google(7)

    if globalvars.phrase.lower().startswith("search google for ")
        google(18)

    if globalvars.phrase.lower().startswith("search the web for ")
        google(19)

    if globalvars.phrase.lower().startswith("search the internet for ")
        google(24)