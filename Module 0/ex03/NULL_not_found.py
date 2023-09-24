def	NULL_not_found(object: any) -> int:
	type_ret = type(object)
	if (object is None):
		print("Nothing: {0} {1}".format(object, type_ret))
	elif (object != object):
		print("Cheese: {0} {1}".format(object, type_ret))
	elif (object is False):
		print("Fake: {0} {1}".format(object, type_ret))
	elif (object == 0):
		print("Zero: {0} {1}".format(object, type_ret))
	elif (isinstance(object, str) and not (object and object.isprintable())):
		print("Empty: {0}".format(type_ret))
	else:
		print("Type not Found")
		return (1)
	return (0)
