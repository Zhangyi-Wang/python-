# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:20:48 2021

@author: WZY
"""
#8.8

def make_album(singer, name, song_number = ''):
    result = {}
    if song_number:
        result[singer] = [name, song_number]
    else:
        result[singer] = name
        
    return result

'''
错误代码：enter q to quit 出现位置不对
while True:
    singer = input('What is the name of the singer? ')
    print('Enter q to quit')
    if singer == 'q':
        break
'''    
#正确代码：
while True:
    print('\nEnter q to quit')
    
    singer = input('What is the name of the singer? ')
    if singer == 'q':
        break
    
    name = input ('What is the name of the album? ')
    if name == 'q':
        break
    
    result = make_album (singer, name)
    print(result)
