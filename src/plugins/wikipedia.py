import sys
import webbrowser
import plugins


def main():

    # search wikipedia
    if plugins.phrase.lower().startswith("search wikipedia for "):
        url = "https://en.wikipedia.org/w/index.php?search=" + plugins.phrase[21:] + "&title=Special%3ASearch"
        webbrowser.open(url)
        print "Searching Wikipedia for \"" + plugins.phrase[21:] + "\""
        sys.exit(0)
    if plugins.phrase.lower().startswith("look on wikipedia for ") or \
    plugins.phrase.lower().startswith("look on wikipedia for "):
        url = "https://en.wikipedia.org/w/index.php?search=" + plugins.phrase[22:] + "&title=Special%3ASearch"
        webbrowser.open(url)
        print "Searching Wikipedia for \"" + plugins.phrase[22:] + "\""
        sys.exit(0)

    # open wikipedia
    if plugins.phrase.lower().startswith("open wikipedia"):
        webbrowser.open("http://en.wikipedia.com/")
        print "Opening Wikipedia"
        sys.exit(0)
