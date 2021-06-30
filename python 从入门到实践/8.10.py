# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:43:06 2021

@author: WZY
"""

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    while magicians:
        #移除magicians到great_magicians
        current_magician = magicians.pop()
        great_magician = 'the Great' + current_magician
        great_magicians = []
        great_magicians.append(great_magician)
        
    #移动到magicians
    for great_magician in great_magicians:
        magicians.append(great_magician)
        
magicians =['david','liu','jide']
make_great(magicians)
show_magicians(magicians)