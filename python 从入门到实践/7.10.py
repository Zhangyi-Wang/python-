# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:37:53 2021

@author: WZY
"""

#7.10

result = {}

active = True

#收集用户名字和答案
while active:
    name = input('What is your name? ')
    place = input('What place would you like to travel? ')
    
    #储存答案
    result[name] = place
    
    #询问用户是否结束
    repeat = input('Would you like to take another poll? (yes/no) ')
    if repeat == 'no':
        active = False
    
#打印结果
print('\n----result:')
for name , place in result.items():
    print(name + " 's favourite place is: " + place)