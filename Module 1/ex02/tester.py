from load_image import ft_load

errors = [
    "landscap.jpg", "errors/blah.jpg",
    "errors/landscape_noread.jpg", "errors/blah.txt"
]

for x in errors:
	print(ft_load(x))

print(ft_load("landscape.jpg"))