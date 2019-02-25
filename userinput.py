correct = False
name = input("Hey person, what is your name?: ")

while correct is not True:
	has_digit = False
	name_length = len(name)
	while name_length > 0:
		for char in name:
			if char.isdigit():
				has_digit = True
			name_length -= 1
	if has_digit is True:
		print("The string you entered contains a number which is not valid!")
		name = input("Hey person, what is your name?: ")
	else:
		print(f"Your name is {name}")
		correct = True
