# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:32:54 2021

@author: WZY
"""

#7.8

sandwich_orders = ['fish','apple','tuna']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your ' + current_sandwich + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

#显示所有完成的三明治
print('\nFinished sandwiches: ')
for finished_sandwich in finished_sandwiches: 
    print(finished_sandwich)
    
#7.9

sandwich_orders = ['fish','pastrami','apple','pastrami','tuna','pastrami']
finished_sandwiches = []

#告诉顾客熏牛肉么得了
print('Sorry, the pstrami has sold out.')

#开始remove所有pasrami
while 'pastrmi' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#移动到finished里
for sandwich in sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

#打印所有finished sandwich
print('Here are the finished sandwiches: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)