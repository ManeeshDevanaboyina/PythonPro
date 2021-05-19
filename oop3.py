# Python program showing a
# use of property() function

class Geeks:
	def __init__(self):
		self._age = 0


	# function to get value of _age
	def get_age(self):
		print("getter method called")
		return self._age

	# function to set value of _age
	def set_age(self, a):
		print("setter method called")
		self._age = a
		return self._age


	# function to delete _age attribute


	#age = property(get_age, set_age, del_age)

mark = Geeks()

print(mark.get_age())
print(mark.set_age(21))
