# exercise from p. 21

# This program says hello and asks for my name
print('Hello world!')
print('What is your name?')	# ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')	# ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')

# exercise from p.43
if myName == 'Alice':
	print('Hi, Alice.')
elif int(myAge) < 12:
	print('You are not Alice, kiddo.')
else: 
	print('You are neither Alice nor a little kid')