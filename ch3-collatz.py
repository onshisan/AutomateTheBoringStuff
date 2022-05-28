def collatz(number):
	
	if number % 2 == 0:
		# Even number
		result = number // 2
	elif number % 2 ==1:
		# Odd number
		result = 3 * number + 1
	
	print(result)
	return result

def main():

	while True:
		try:
			number = int(input('Enter a number:'))
			break
		except ValueError:
			print("That wasn't an integer.")
			continue

	while True:
		number = collatz(number)
		if number == 1:
			break

main()