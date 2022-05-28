import sys

while True:
	print('Type exit to exit.')
	response = input()
	if response == 'exit':
		# Exit program upon correct user input
		sys.exit()
	print('You typed ' + response + '.')
