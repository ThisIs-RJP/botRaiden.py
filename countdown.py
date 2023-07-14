#!/usr/bin/env python3

"""
    This is the countdown Python file that will run along side the main.py
    Run main.py and this will constantly loop looking for countdowns
"""

import datetime
from config import *

def checkThis(time):
    print(time)
    check = ""
    checkTime = time.split(";")

    for d in time:
        if d.isdigit():
            check = check + "0"
        
        elif d == "-" or d == ":" or d == ";" or d == " ":
            check = check + d
        
        else:
            pass

    check = check.strip()
    print(check)

    if check != "0000-00-00 00:00:00 ;":
        return makeEmbed("Incorrect format", False, "There is an incorrect event at time **{}**".format(time), "Please try again")
    
    else:
        return "c" + time

print("The clock is ticking...")
file = "cogs/times.txt"


