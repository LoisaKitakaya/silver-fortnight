"""

Perimeter

The perimeter of a shape is the total length of its sides. \
    The formula for calculating the perimeter depends on the shape.

"""

"""

Rectangle

the formula for calculating the perimeter of a rectangle is:

P = 2(l + w) where P is perimeter, l is length, and w is width.

"""


def rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)

    return perimeter


"""

Circle

the formula for calculating the perimeter of a circle is:

P = 2πr where P is perimeter, and r is radius.

"""


def circle_perimeter(radius):
    pi = 3.14159

    circumference = 2 * (pi * radius)

    circumference = round(circumference, 5)

    return circumference


"""

Triangle

the formula for calculating the perimeter of a triangle is:

P = a + b + c where P is perimeter, and a, b, and c are the lengths of the sides.

"""


def triangle_perimeter(side_1, side_2, side_3):
    perimeter = side_1 + side_2 + side_3

    return perimeter


"""

Area

The area of a shape is the amount of space it occupies. \
    The formula for calculating the area also depends on the shape.

"""

"""

Rectangle

the formula for calculating the area of a rectangle is:

A = lw where A is area, l is length, and w is width.

"""


def rectangle_area(length, width):
    area = length * width

    return area


"""

Circle

the formula for calculating the area of a circle is:

A = πr^2 where A is area, and r is radius.

"""


def circle_area(radius):
    pi = 3.14159

    area = pi * (radius**2)

    area = round(area, 5)

    return area


"""

Triangle

the formula for calculating the area of a triangle is:

A = 1/2bh where A is area, b is the base, and h is the height.

"""


def triangle_area(base, height):
    area = 0.5 * (base * height)

    return area


"""

Volume

The volume of a shape is the amount of space it occupies in three dimensions. \
    The formula for calculating the volume also depends on the shape.

"""

"""

Cube

the formula for calculating the volume of a cube is:

V = s^3 where V is volume, and s is the length of the side.

"""


def cube_volume(side):
    volume = side**3

    return volume


"""

Cylinder

the formula for calculating the volume of a cylinder is:

V = πr^2h where V is volume, r is radius, and h is height.

"""


def cylinder_volume(radius, height):
    pi = 3.14159

    volume = (pi * (radius**2)) * height

    volume = round(volume, 5)

    return volume


"""

Sphere

the formula for calculating the volume of a sphere is:

V = 4/3πr^3 where V is volume, and r is radius.

"""


def sphere_volume(radius):
    pi = 3.14159

    volume = (4 / 3) * (pi * (radius**3))

    volume = round(volume, 5)

    return volume
