import sys
import webbrowser
import plugins

def main():
    
    # search youtube
    if plugins.phrase.lower().startswith("search youtube for ") or \
    plugins.phrase.lower().startswith("look on youtube for "):
        url = "https://www.youtube.com/results?search_query=" + plugins.phrase[19:]
        webbrowser.open(url)
        print "Searching YouTube for \"" + plugins.phrase[19:] + "\""
        sys.exit(0)
    if plugins.phrase.lower().startswith("find videos on ") or \
    plugins.phrase.lower().startswith("find videos of "):
        url = "https://www.youtube.com/results?search_query=" + plugins.phrase[15:]
        webbrowser.open(url)
        print "Searching YouTube for \"" + plugins.phrase[15:] + "\""
        sys.exit(0)

    # open youtube
    if plugins.phrase.lower() == "open youtube" or plugins.phrase.lower() == "open you tube" or plugins.phrase.lower() == "open youtube.com":
        webbrowser.open("http://youtube.com/")
        print "Opening YouTube"
        sys.exit(0)