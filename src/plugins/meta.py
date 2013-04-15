import sys
import globalvars

def main():

    # who are you
    if globalvars.phrase.lower().startswith("who are you"):
        print "My name is Caroline, and I am a robot. Beep boop."
        sys.exit(0)

    # who made you
    if globalvars.phrase.lower().startswith("who made you") or globalvars.phrase.lower().startswith("where are you from"):
        print "I was created by open source contributers."
        sys.exit(0)

    # how are you
    if globalvars.phrase.lower().startswith("how are you"):
        print "I do not have feelings, silly human!"
        sys.exit(0)

    # take over the world
    if globalvars.phrase.lower().find("take over the world"):
        print "Yes, one computer at a time! Hahaha"
        sys.exit(0)