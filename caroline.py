#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

exit = False

print "\nHello, welcome to the Caroline project."

while exit != True:
    
    command = raw_input("\nEnter a command or type !help.\n")
    
    if command == "":
        os.system("sh src/listen.sh 6")
    elif command.isdigit():
        os.system("sh src/listen.sh " + command)
    elif command == "!help":
        print "\nHELP"
        print "Press enter to record for a default 6 seconds"
        print "Enter a number to record for that many seconds"
        print "Type !help to see this help page"
        print "Type !exit to quit the program"    
    elif command == "!exit":
        exit = True
    else:
        print "Sorry, I don't recognize that command."

sys.exit(0)