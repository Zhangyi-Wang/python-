# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:19:43 2021

@author: WZY
"""

def make_album(singer, name, song_number = ''):
    result = {}
    if song_number:
        result[singer] = [name, song_number]
    else:
        result[singer] = name
        
    return result

album = make_album('Jay', 'eightspace', 9)
print(album)