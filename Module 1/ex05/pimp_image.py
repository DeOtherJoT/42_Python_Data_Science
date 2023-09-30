import numpy as np
import matplotlib.pylab as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    '''Inverts the colours of the image given'''
    if array is None:
        raise AssertionError("ft_load must be given a valid image.")
    res = 255 - array
    print("Image with inverted filter size:", res.shape)

    plt.imshow(res)
    plt.show()


def ft_red(array: np.ndarray) -> np.ndarray:
    '''Applies a red filter to the image'''
    if array is None:
        raise AssertionError("ft_load must be given a valid image.")
    red = array[:, :, 0]
    green = array[:, :, 1] * 0
    blue = array[:, :, 2] * 0

    res = np.stack((red, green, blue), axis=-1)
    print("Image with red filter size:", res.shape)

    plt.imshow(res)
    plt.show()


def ft_green(array: np.ndarray) -> np.ndarray:
    '''Applies a green filter to the image'''
    if array is None:
        raise AssertionError("ft_load must be given a valid image.")
    red = array[:, :, 0] - array[:, :, 0]
    green = array[:, :, 1]
    blue = array[:, :, 2] - array[:, :, 2]

    res = np.stack((red, green, blue), axis=-1)
    print("Image with green filter size:", res.shape)

    plt.imshow(res)
    plt.show()


def ft_blue(array: np.ndarray) -> np.ndarray:
    '''Applies a blue filter to the image'''
    if array is None:
        raise AssertionError("ft_load must be given a valid image.")
    res = np.zeros(array.shape, dtype=int)
    res[:, :, 2] = array[:, :, 2]
    print("Image with blue filter size:", res.shape)

    plt.imshow(res)
    plt.show()


def ft_grey(array: np.ndarray) -> np.ndarray:
    '''Applies the grey filter to the image'''
    if array is None:
        raise AssertionError("ft_load must be given a valid image.")
    res = np.array(np.dot(array[..., :3], [0.299, 0.587, 0.114]))
    print("Image with grey filter size:", res.shape)

    plt.imshow(res, cmap='grey')
    plt.show()
