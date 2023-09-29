import numpy as np
import matplotlib.pylab as plt
from PIL import UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:

    try:
        assert (type(path) == str), "Argument must be a string."
    except AssertionError as e:
        print("AssertionError:", e)
        return

    try:
        image = plt.imread(path)
        print("The shape of the image is : {}".format(image.shape))
        return (image.reshape(1,-1,3))
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    except PermissionError as e:
        print("PermissionError:", e)
    except UnidentifiedImageError as e:
        print("UnidentifiedImageError: ", e)
