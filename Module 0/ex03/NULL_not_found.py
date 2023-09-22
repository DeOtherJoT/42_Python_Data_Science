def	NULL_not_found(object: any) -> int:
	type_ret = type(object)
	if (object is None):
		print("Nothing: {0} {1}".format(object, type_ret))
	elif (type_ret == float):
		print("Cheese: {0} {1}".format(object, type_ret))
	elif (type_ret == int):
		print("Zero: {0} {1}".format(object, type_ret))
	elif (type_ret == str):
		print("Empty: {0}".format(type_ret))
	elif (type_ret == bool):
		print("Fake: {0} {1}".format(object, type_ret))
	else:
		print("Type not Found")
		return (1)
	return (0)

target = False
print(type(target))
print(target)
NULL_not_found(target)