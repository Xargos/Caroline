import sys
import webbrowser
import globalvars

def main():
    
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