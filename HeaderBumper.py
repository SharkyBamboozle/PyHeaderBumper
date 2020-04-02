#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""The code was hard to write it should be hard to read. Small code golfing 
exercise condensing the functionality into as few lines as possible (and also 
as square as possible) unfortunately yielding incomprehensible source code."""

__author__    = 'Julius Mayer'
__email__     = 'jmayer@shell.ink'
__date__      = '01.09.2019'
__copyright__ = '(C) 2019 Julius Mayer'
__license__   = 'Open Domain'


#==============================================================================#
#========================|          Imports           |========================#
#==============================================================================#

#standard library imports
from datetime import datetime


#==============================================================================#
#===================|          Header Bumper v2.0          |===================#
#==============================================================================#

def HeaderBumper(title="Header Bumper v2.0", marker="#", indent=0, time=False):
    """Create a fashionable header bumper with an offset for arbitrary function 
    indentation and optional time of creation signature. Can serve to visually
    group and organise your src code or print prominent flags to the terminal. 
    
    @param  title:  title to be displayed in the banner middle
    @param  marker: comment character to mark banner as such (e.g. Latex '%') 
    @param  indent: the number of function indentation level to be considered
    @param  time:   whether or not to include the current time in the banner
    @return:        the three lines of the header to be copied or printed"""

    assert indent < 9,"Syntax can't support indentation level higher than eight"
    bumper = HeaderBumper(title,marker,indent-1,time) +"\n \n" if indent else ""
    if indent *8 +len(title) > 72: title = title[:max(0, 69 -indent *8)] + "..."
    title += "" if len(title) % 2 == 0 else " "
    banner, gap ="\t"*indent+marker+"="*(39-indent*4),"|"+" "*int(10/(indent+1))
    banner += banner[::-1]+"\n"+banner[:int(max(40-indent*3-len(title)/2-len(gap
        ),indent+2))] +gap[:int(max(2,min(len(gap), 38-indent*4-len(title)/2)))]
    time ="<{}>".format(datetime.now().strftime('%H:%M:%S')) if time else "="*12
    pos = banner[80 -indent *6:].count("=") +indent +11
    return bumper+(banner+title.title()+banner[:pos:-1]+time+banner[pos-10::-1])


#==============================================================================#
#==========================|          Main          |==========================#
#==============================================================================#

if __name__ == '__main__':

    title = "- Your fashionable Header-Bumper Title -"
    print(HeaderBumper(title, indent=8, time=True))