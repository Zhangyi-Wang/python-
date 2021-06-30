# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:25:48 2021

@author: WZY
"""
#6.8
print('6.8')
xiaotian = {'master':'erlangshen','type':'dog'}
jiafei = {'master':'a','type':'cat'}
#创建列表
pets = [xiaotian, jiafei]
for pet in pets:
    print(pet)

print('\n6.9')

#6.9
'''
这里有个遍历列表的技巧：
'''
favourite_places = {
    'a':['yangzhou','shanghai'],
    'b':['wuxi','nanjing','beijing'],
    'c':['hongkong']}

#错误代码：print (name+"'s favourite places are: " + p in place)
for name,place in favourite_places.items():
    print(name+"'s favourite places are: ")
    for p in place:
        print(p)

print('\n6.10')  
      
#6.10
cities = {
    'yangzhou':{'country':'China','Province':'Jiangsu'},
    'Nanjing':{'country':'China','Province':'Jiangsu'},
    'Shanghai':{'country':'China','Province':'Shanghai'}
    }

for city, info in cities.items():
    print('\n'+city)
    for key,values in info.items():
        print(key+': '+values)
#如果这里print('\n')就会出现两行，所以正确的方法是在上面print(\n'+city)
#在一个print立马就不会自动换行
