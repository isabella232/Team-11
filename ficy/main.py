
def age_selector(self):
	print("Welcome to FICY! We are comitted to spreading financial literacy to everyone around the world!\n")
	age = eval(input("To begin, please enter your age: "))
	if age < 13:
		return kids.self()
	if age => 13 and age <= 35:
		return young_adults.self()
	if age > 35 and age < 65:
		return adults.self()
	if age => 65:
		return elderly.self()


def kids(self):


def young_adults(self):


def adults(self):


def elderly(self):