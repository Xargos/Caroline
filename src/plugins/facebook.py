import sys
import webbrowser
import plugins


def main():

    # open facebook
    if plugins.phrase.lower().startswith("open facebook") or plugins.phrase.lower().startswith("open face book"):
        webbrowser.open("http://facebook.com/")
        print "Opening Facebook"
        sys.exit(0)

    # open my facebook
    if plugins.phrase.lower().startswith("open my facebook") or plugins.phrase.lower().startswith("open my face book"):
        webbrowser.open("http://facebook.com/profile.php")
        print "Opening your Facebook profile page"
        sys.exit(0)
