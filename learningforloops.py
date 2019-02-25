my_first_list = [1, 2, 3]
my_second_list = ["one", "two", "three"]
my_first_dictionary = {}
my_first_dictionary["father"] = "dad"
my_first_dictionary["mother"] = "mom"
my_third_list = []
my_third_list.append(my_first_list)
my_third_list.append(my_second_list)
my_third_list.append(my_first_dictionary)
my_fourth_list = []
my_fourth_list.append(my_third_list)

for item in my_fourth_list:
	print(item)
