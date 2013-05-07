import sys
import webbrowser
import plugins


def main():

    # graph function
    if plugins.phrase.lower().startswith("graph "):
        url = "http://graph.tk/#" + plugins.phrase[6:]
        webbrowser.open(url)
        print "Graphing \"" + plugins.phrase[6:] + "\""
        sys.exit(0)

    # open graph.tk
    if plugins.phrase.lower().startswith("open graph"):
        webbrowser.open("http://youtube.com/")
        print "Opening Graph.tk"
        sys.exit(0)
