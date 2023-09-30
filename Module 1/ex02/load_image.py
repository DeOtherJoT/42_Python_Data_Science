import numpy as np
import matplotlib.pylab as plt
from PIL import UnidentifiedImageError
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    '''Function that loads an image located in <path>'''

    try:
        assert (type(path) == str), "Argument must be a string."
    except AssertionError as e:
        print("AssertionError:", e)
        return

    try:
        image = plt.imread(path)
        alt = Image.open(path)
        print("The format of the image is : {}".format(alt.format))
        print("The shape of the image is : {}".format(image.shape))
        return (image.reshape(1,-1,3))
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    except PermissionError as e:
        print("PermissionError:", e)
    except UnidentifiedImageError as e:
        print("UnidentifiedImageError:", e)
    except SyntaxError as e:
        print("SyntaxError:", e)
