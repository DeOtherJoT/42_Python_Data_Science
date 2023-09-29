from load_image import ft_load

errors = [
    "landscap.jpg", "errors/blah.jpg",
    "errors/landscape_noread.jpg", "errors/blah.txt",
	"errors/landscape.png"
]

for x in errors:
	print(ft_load(x))

test = ft_load("landscape.jpg")
print(test)