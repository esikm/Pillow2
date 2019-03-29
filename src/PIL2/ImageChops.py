#
# The Python Imaging Library.
# $Id$
#
# standard channel operations
#
# History:
# 1996-03-24 fl   Created
# 1996-08-13 fl   Added logical operations (for "1" images)
# 2000-10-12 fl   Added offset method (from Image.py)
#
# Copyright (c) 1997-2000 by Secret Labs AB
# Copyright (c) 1996-2000 by Fredrik Lundh
#
# See the README file for information on usage and redistribution.
#

from . import Image


def constant(image, value):
    """Fill a channel with a given grey level.

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    return Image.new("L", image.size, value)


def duplicate(image):
    """Copy a channel. Alias for :py:meth:`PIL2.Image.Image.copy`.

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    return image.copy()


def invert(image):
    """
    Invert an image (channel).

    .. code-block:: python

        out = MAX - image

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image.load()
    return image._new(image.im.chop_invert())


def lighter(image1, image2):
    """
    Compares the two images, pixel by pixel, and returns a new image containing
    the lighter values.

    .. code-block:: python

        out = max(image1, image2)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_lighter(image2.im))


def darker(image1, image2):
    """
    Compares the two images, pixel by pixel, and returns a new image
    containing the darker values.

    .. code-block:: python

        out = min(image1, image2)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_darker(image2.im))


def difference(image1, image2):
    """
    Returns the absolute value of the pixel-by-pixel difference between the two
    images.

    .. code-block:: python

        out = abs(image1 - image2)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_difference(image2.im))


def multiply(image1, image2):
    """
    Superimposes two images on top of each other.

    If you multiply an image with a solid black image, the result is black. If
    you multiply with a solid white image, the image is unaffected.

    .. code-block:: python

        out = image1 * image2 / MAX

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_multiply(image2.im))


def screen(image1, image2):
    """
    Superimposes two inverted images on top of each other.

    .. code-block:: python

        out = MAX - ((MAX - image1) * (MAX - image2) / MAX)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_screen(image2.im))


def add(image1, image2, scale=1.0, offset=0):
    """
    Adds two images, dividing the result by scale and adding the
    offset. If omitted, scale defaults to 1.0, and offset to 0.0.

    .. code-block:: python

        out = ((image1 + image2) / scale + offset)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_add(image2.im, scale, offset))


def subtract(image1, image2, scale=1.0, offset=0):
    """
    Subtracts two images, dividing the result by scale and adding the
    offset. If omitted, scale defaults to 1.0, and offset to 0.0.

    .. code-block:: python

        out = ((image1 - image2) / scale + offset)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_subtract(image2.im, scale, offset))


def add_modulo(image1, image2):
    """Add two images, without clipping the result.

    .. code-block:: python

        out = ((image1 + image2) % MAX)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_add_modulo(image2.im))


def subtract_modulo(image1, image2):
    """Subtract two images, without clipping the result.

    .. code-block:: python

        out = ((image1 - image2) % MAX)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_subtract_modulo(image2.im))


def logical_and(image1, image2):
    """Logical AND between two images.

    .. code-block:: python

        out = ((image1 and image2) % MAX)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_and(image2.im))


def logical_or(image1, image2):
    """Logical OR between two images.

    .. code-block:: python

        out = ((image1 or image2) % MAX)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_or(image2.im))


def logical_xor(image1, image2):
    """Logical XOR between two images.

    .. code-block:: python

        out = ((bool(image1) != bool(image2)) % MAX)

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    image1.load()
    image2.load()
    return image1._new(image1.im.chop_xor(image2.im))


def blend(image1, image2, alpha):
    """Blend images using constant transparency weight. Alias for
    :py:meth:`PIL2.Image.Image.blend`.

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    return Image.blend(image1, image2, alpha)


def composite(image1, image2, mask):
    """Create composite using transparency mask. Alias for
    :py:meth:`PIL2.Image.Image.composite`.

    :rtype: :py:class:`~PIL2.Image.Image`
    """

    return Image.composite(image1, image2, mask)


def offset(image, xoffset, yoffset=None):
    """Returns a copy of the image where data has been offset by the given
    distances. Data wraps around the edges. If **yoffset** is omitted, it
    is assumed to be equal to **xoffset**.

    :param xoffset: The horizontal distance.
    :param yoffset: The vertical distance.  If omitted, both
        distances are set to the same value.
    :rtype: :py:class:`~PIL2.Image.Image`
    """

    if yoffset is None:
        yoffset = xoffset
    image.load()
    return image._new(image.im.offset(xoffset, yoffset))
