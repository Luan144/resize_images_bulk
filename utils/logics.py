from PIL import Image, ImageOps


def resize_with_padding(img, expected_size: tuple[int,int]):
    """
    Calculates the image's ratio and resizes the image by adding a
    zero-padding to it without changing the ratio.
    """
    img.thumbnail((expected_size[0], expected_size[1]), Image.LANCZOS)
    width_var = expected_size[0] - img.size[0]
    height_var = expected_size[1] - img.size[1]
    pad_width = width_var // 2
    pad_height = height_var // 2
    padding = (pad_width,
               pad_height,
               width_var - pad_width,
               height_var - pad_height)

    return ImageOps.expand(img, padding)


def resize_without_padding(img, expected_size):
    """
    Resizes the image changing its ratio.
    """

    return img.resize(size=expected_size, resample=Image.LANCZOS)
