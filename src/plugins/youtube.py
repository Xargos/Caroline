import sys
import webbrowser
import globalvars

def main():
    
    # search youtube
    if globalvars.phrase.lower().startswith("search youtube for ") or \
    globalvars.phrase.lower().startswith("look on youtube for "):
        url = "https://www.youtube.com/results?search_query=" + globalvars.phrase[19:]
        webbrowser.open(url)
        print "Searching YouTube for \"" + globalvars.phrase[19:] + "\""
        sys.exit(0)
    if globalvars.phrase.lower().startswith("find videos on ") or \
    globalvars.phrase.lower().startswith("find videos of "):
        url = "https://www.youtube.com/results?search_query=" + globalvars.phrase[15:]
        webbrowser.open(url)
        print "Searching YouTube for \"" + globalvars.phrase[15:] + "\""
        sys.exit(0)

    # open youtube
    if globalvars.phrase.lower() == "open youtube" or globalvars.phrase.lower() == "open you tube" or globalvars.phrase.lower() == "open youtube.com":
        webbrowser.open("http://youtube.com/")
        print "Opening YouTube"
        sys.exit(0)