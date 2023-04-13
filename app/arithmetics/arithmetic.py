from functools import reduce
import math

"""

addition (sum) function

this function takes a tuple of integers or floats and returns the sum of the values

"""


def arithmetic_sum(*args):
    try:
        total = reduce(lambda x, y: x + y, args)

    except Exception as e:
        raise Exception(str(e))

    return total


"""

subtraction (difference) function

this function takes a tuple of integers or floats and returns the difference between the values

"""


def arithmetic_difference(*args):
    try:
        difference = reduce(lambda x, y: x - y, args)

    except Exception as e:
        raise Exception(str(e))

    return difference


"""

multiply (multiplication) function

this function takes a tuple of integers or floats and returns the multiplication between the values

"""


def arithmetic_multiplication(*args):
    try:
        multiplication = reduce(lambda x, y: x * y, args)

    except Exception as e:
        raise Exception(str(e))

    return multiplication


"""

divide (division) function

this function takes a tuple of integers or floats and returns the division between the values

"""


def arithmetic_division(*args):
    try:
        division = reduce(lambda x, y: x / y, args)

    except Exception as e:
        raise Exception(str(e))

    return division


"""

exponent (exponentiation) function

this function takes a tuple of integers or floats and raises the first operand \
    to the power of the second operand

"""


def arithmetic_exponent(*args):
    try:
        exponential = reduce(lambda x, y: x**y, args)

    except Exception as e:
        raise Exception(str(e))

    return exponential


"""

square (square root) function

this function takes a type integer or float and returns the square root of the number

"""


def arithmetic_root(number):
    try:
        root = math.sqrt(number)

    except Exception as e:
        raise Exception(str(e))

    return root


"""

floor (floor division) function

this function takes a tuple of integers or floats and returns the largest integer \
    that is less than or equal to the result of dividing the two operands

here the quotient is rounded down to the nearest integer

"""


def arithmetic_floor(*args):
    try:
        floor = reduce(lambda x, y: x // y, args)

    except Exception as e:
        raise Exception(str(e))

    return floor


"""

modulo (modulo division) function

this function takes a tuple of integers or floats and returns the remainder of dividing \
    the first operand by the second operand

"""


def arithmetic_modulo(*args):
    try:
        modulo = reduce(lambda x, y: x % y, args)

    except Exception as e:
        raise Exception(str(e))

    return modulo
