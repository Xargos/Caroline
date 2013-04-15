import sys
import webbrowser
import plugins

def google(letters):
    url = "https://encrypted.google.com/search?hl-en&q=" + plugins.phrase[letters:]
    webbrowser.open(url)
    print "Googling \"" + plugins.phrase[letters:] + "\""
    sys.exit(0)

def translate(letters):
    url = "http://translate.google.com/#auto/en/" + plugins.phrase[letters:]
    webbrowser.open(url)
    print "Translating \"" + plugins.phrase[letters:] + "\""
    sys.exit(0)

def main():

    # google web search
    if plugins.phrase.lower().startswith("google "):
        google(7)
    if plugins.phrase.lower().startswith("search google for "):
        google(18)
    if plugins.phrase.lower().startswith("search the web for "):
        google(19)
    if plugins.phrase.lower().startswith("search the internet for "):
        google(24)

    # open google
    if plugins.phrase.lower() == "open google" or plugins.phrase.lower() == "open google.com":
        webbrowser.open("https://google.com/")
        print "Opening Google"
        sys.exit(0)

    # google drive
    if plugins.phrase.lower() == "open google drive" or plugins.phrase.lower() == "open google documents":
        webbrowser.open("https://drive.google.com/")
        print "Opening Google Drive"
        sys.exit(0)

    # google translate
    if plugins.phrase.lower() == "open google translate":
        webbrowser.open("http://translate.google.com/")
        print "Opening Google Translate"
        sys.exit(0)
    if plugins.phrase.lower() == "open gmail" or plugins.phrase.lower() == "open google mail":
        webbrowser.open("https://mail.google.com/mail/")
        print "Opening Google Mail"
        sys.exit(0)
    if plugins.phrase.lower().startswith("google translate "):
        translate(17)
    if plugins.phrase.lower().startswith("translate "):
        translate(10)