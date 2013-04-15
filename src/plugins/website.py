import sys
import webbrowser
import plugins

def main():

    # open website
    if plugins.phrase.lower().startswith("go to "):
        webbrowser.open('http://' + plugins.phrase[6:])
        print "Opening " + plugins.phrase[6:]
        sys.exit(0)