""" def main():
	my_list = [
	  '2',
	  'Hello'
	]
	index_to_use = 4
	
	list_element_to_convert = '0'
	element_to_int = 0
	try:
		list_element_to_convert = my_list[index_to_use]
		element_to_int = int(list_element_to_convert)
		print(list_element_to_convert)
	except Exception as error:
		print(f'Ha ocurrido un error: {error}')
	
	print(list_element_to_convert)


if __name__ == '__main__':
	main()
 
## 
def ask_for_user_information():
	try:
		age = int(input('Ingrese su edad'))
		if age < 1 or age > 100:
			raise ValueError()

	except ValueError as ex:
		print("Ingrese una edad valida!")
		raise ex


def main():
	try:
		ask_for_user_information()
		# create_order()

	except Exception as ex:
		exit()


if __name__ == '__main__':
	main()
  """
 ##
def check_if_number_is_100(number):
	if number < 100:
		raise ValueError('El numero es muy bajo')
	elif number > 100:
		raise ValueError('El numero es muy alto')
	
	return True

def main():
	number = input('Ingrese un numero')
	try:
		number_int = int(number)
		check_if_number_is_100(number_int)
	except ValueError as ex:
		print(ex)


if __name__ == '__main__':
	main() 