# This program says hello and asks for my name

print ('Hello world')
print ('What is your first name?') # ask for their name
myName = input()
print ('It is good to meet you, ' + myName + '.' + ' What is your last name?') # ask for last name
myLastName = input()
whoYouAre = myName + ' ' + myLastName
print('It is good to meet you, ' + whoYouAre)
print('The length of your name is:')
print(len(whoYouAre))
print('What is your age?') #ask for age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
