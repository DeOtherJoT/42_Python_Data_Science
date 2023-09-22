def	all_thing_is_obj(object: any) -> int:
	type_ret = type(object)
	if (type_ret == list):
		print("List : " + format(type_ret))
	elif (type_ret == tuple):
		print("Tuple : " + format(type_ret))
	elif (type_ret == set):
		print("Set : " + format(type_ret))
	elif (type_ret == dict):
		print("Dict : " + format(type_ret))
	elif (type_ret == str):
		print("{0} is in the kitchen : {1}".format(object, type_ret))
	else:
		print("Type not found")
	return (42)