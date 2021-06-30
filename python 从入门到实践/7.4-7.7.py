# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:12:37 2021

@author: WZY
"""
#7.4 
'''
错误示范1
topping = input('please enter your toppings: ')
while topping != 'quit':
    print('We will add ' + topping +' in your pizza')
'''

'''错误示范2
topping = input('please enter your toppings: ')
while topping != 'quit':
    print('We will add ' + topping +' in your pizza')
    topping = input(topping)
'''

prompt = '\nPlease enter your toppings: '
prompt += '\nenter quit to end the program. '
topping = ''
while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print('We will add '+topping+' into your pizza.')

'''
让用户输入是在循环里的，所以在开头定义prompt，
while里input(prompt),这样每循环一次都会问
'''

#7.5
prompt = 'Tell me your age: '
while True:
    age = input (prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age <3:
            print('The ticket is free.')
        elif age < 12:
            print ('The ticket is 10 dollors.')
        elif age > 12:
            print ('The ticket is 15 dollors.')
        
#7.6
#用while条件测试
prompt = 'Tell me your toppings: '
prompt += 'Enter quit to end the program.'
message = ''
while message != 'quit':
    message = input(prompt) 
    if message != 'quit':
        print('I will add '+topping+'onto your pizza.')

#用active
prompt = 'Tell me your toppings: '
prompt += '\nEnter quit to end the program.'
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print('We will add '+ message + ' on your pizza.')

#用break
prompt = 'Tell me your toppings: '
prompt += '\nEnter quit to end the program.'
while True:
    message = input(prompt)
    if message =='quit':
        break
    print('We will add '+ message + ' on your pizza.')