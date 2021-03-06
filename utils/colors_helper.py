""" Colors helpers

.. moduleauthor:: `Marie FETIVEAU <github.com/mfe>`_

"""
__version__ = "0.1"
import math


def xy_to_XYZ(xy, Y=1):
    """Convert xyY into XYZ

    Args:
        xy ([float, float]): x, y input values

    Kwargs:
        Y (float): Y input value

    Returns:
        .[float, float, float]

    """
    x, y = xy
    X = (x * Y) / y
    Z = ((1 - x - y) * Y) / y
    return [X, Y, Z]


def xy_to_upvp(xy):
    """Convert xy to u'v'

    Args:
        xy ([float, float]): x, y input values

    Returns:
        .[float, float]
    """
    x, y = xy
    up = 4 * x / (-2 * x + 12 * y + 3)
    vp = 9 * y / (-2 * x + 12 * y + 3)
    return [up, vp]


def lin_to_gamma(value, gamma):
    """Simple lin to Gamma function

    Args:
        value (float): input value

        gamma (float): gamma value

    Returns:
        .float

    """
    return math.pow(value, 1 / gamma)


def gamma_to_lin(value, gamma):
    """Simple gamma to lin function

    Args:
        value (float): input value

        gamma (float): gamma value

    Returns:
        .float

    """
    return math.pow(value, gamma)
