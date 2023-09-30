import numpy as np
import matplotlib.pylab as plt
from load_image import ft_load


def zoom(image: np.ndarray) -> np.ndarray:
    '''Crops the image by half, around the centre of the image and converts
    it to grayscale.'''

    if image is None:
        raise AssertionError("ft_load must return a valid image.")

    # cropping
    x, y = image.shape[0], image.shape[1]
    crop = image[x//4:-x//4, y//4:-y//4]

    # grayscaling
    gray = np.array(np.mean(crop, -1))
    g_3D = gray[:, :, np.newaxis]

    # printouts
    print(image.reshape(1, -1, 3))
    print(f"New shape after slicing: {g_3D.shape} or {gray.shape}")
    print(gray.reshape(1, -1, 1))

    plt.imshow(gray, cmap=plt.get_cmap('grey'))
    plt.show()


def main():
    '''Main driver function'''
    img = ft_load('animal.jpeg')
    zoom(img)


if __name__ == "__main__":
    main()
