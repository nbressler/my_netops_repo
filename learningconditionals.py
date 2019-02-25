my_integer = 443
if my_integer > 0:
	print("Hey, that looks like a positive number!")

my_integer = -443
if my_integer > 0:
	print("Hey, that looks like a positive number!")

#my_integer = "mmm tacos!"
#if my_integer > 0:
#	print("Hey, that looks like a positive number!")

my_string = "you call that a string"
if "?" in my_string:
	print("Yep! There is a ? in that string")
elif ":" in my_string:
	print("Yep! There is a colon in that string")
elif "strong" in my_string:
	print("Yep! The word string is in that string")
else:
	print("Whoa, we got a catch-all now!")
