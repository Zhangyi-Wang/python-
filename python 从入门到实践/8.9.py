# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:35:55 2021

@author: WZY
"""

#8.9

magicians =['david','liu','jide']
   
#显示魔术师名字
def show_magicians(magicians):
    magicians = make_great(magicians)
    for magician in magicians:
        print(magician)

show_magicians(magicians)