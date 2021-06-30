# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 12:50:26 2021

@author: WZY
"""

rivers = {'nile':'egypt','long_river':'China','Amazon':'Peru'}
#河流流经哪里
for river,country in rivers.items():
    print ('The '+river.title()+' runs through '+
           country.title()+'.')
print('\n')
#提到的河流
for river in rivers:
    print (river)

print('\n')
#提到的地方
for country in rivers.values():
    print(country)