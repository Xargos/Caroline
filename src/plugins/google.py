import sys
import webbrowser
import globalvars

def google(letters):
    url = "https://encrypted.google.com/search?hl-en&q=" + globalvars.phrase[letters:]
    webbrowser.open(url)
    print "Googling \"" + globalvars.phrase[letters:] + "\""
    sys.exit(0)

def translate(letters):
    url = "http://translate.google.com/#auto/en/" + globalvars.phrase[letters:]
    webbrowser.open(url)
    print "Translating \"" + globalvars.phrase[letters:] + "\""
    sys.exit(0)

def main():

    # google web search
    if globalvars.phrase.lower().startswith("google "):
        google(7)
    if globalvars.phrase.lower().startswith("search google for "):
        google(18)
    if globalvars.phrase.lower().startswith("search the web for "):
        google(19)
    if globalvars.phrase.lower().startswith("search the internet for "):
        google(24)

    # google drive
    if globalvars.phrase.lower() == "open google drive" or globalvars.phrase.lower() == "open google documents":
        webbrowser.open("https://drive.google.com/")
        print "Opening Google Drive"
        sys.exit(0)

    # google translate
    if globalvars.phrase.lower() == "open google translate":
        webbrowser.open("http://translate.google.com/")
        print "Opening Google Translate"
        sys.exit(0)
    if globalvars.phrase.lower() == "open gmail" or globalvars.phrase.lower() == "open google mail":
        webbrowser.open("https://mail.google.com/mail/")
        print "Opening Google Mail"
        sys.exit(0)
    if globalvars.phrase.lower().startswith("google translate "):
        translate(17)
    if globalvars.phrase.lower().startswith("translate "):
        translate(10)