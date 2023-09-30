from load_image import ft_load
import numpy as np
import matplotlib.pylab as plt


def ft_zoom(img: np.ndarray) -> np.ndarray:
	'''Crops the image by half, around the centre of the image and converts
	it to grayscale. Returns the numpy array of the result'''

	# grayscaling
	gray = np.array(np.mean(img, -1))

	# cropping
	x, y = gray.shape
	crop = gray[x//4:-x//4, y//4:-y//4]

	# return the cropped and "grayscaled" image as an numpy array
	return (crop)


def ft_transpose(img: np.ndarray) -> np.ndarray:
	'''Takes an image and transposes it to appear like it has been rotated
	by 90 degrees anti-clockwise. Returns the numpy array of the result'''

	# get the size of the current image
	old_x, old_y = img.shape

	# get the size of the resulting image and init
	new_x, new_y = old_y, old_x
	ret = np.zeros([new_x, new_y])

	# rotate it and pray
	for i in range(old_x):
		for j in range(old_y):
			ret[-j][i] = img[i][j]
	
	return (ret)


def main():
	img = ft_load("animal.jpeg")
	if img is None:
		raise AssertionError("ft_load must return a valid array.")
	zoomed = ft_zoom(img)
	print(
		f"The shape of image is: {zoomed[:, :, plt.newaxis].shape}"
		f" or {zoomed.shape}"
	)
	res = ft_transpose(zoomed)
	print(f"New shape after Transpose: {res.shape}")
	print(res)


if __name__ == "__main__":
	main()