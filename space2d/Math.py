import math


def degs_to_rads(degs):
    return degs * (3.14159265358 / 180.0)


def cos(x):
    return math.cos(x)


def sin(x):
    return math.sin(x)


def multiply_vector_by_matrix(vector, matrix):
        return [
                vector[0]*matrix[0][0] + vector[1] * matrix[1][0],
                vector[0]*matrix[0][1] + vector[1] * matrix[1][1]
               ]


def rotate_vector(vector, angle):
    return [
            vector[0] * cos(angle) + vector[1] * sin(angle),
            - vector[0] * sin(angle) + vector[1] * cos(angle)
    ]


def rotate_matrix(m, a):
    sinc = sin(a)
    cosc = cos(a)
    rotated = [
        [m[0][0] * cosc + m[0][1] * sinc,  - m[0][0] * sinc + m[0][1] * cosc],
        [m[1][0] * cosc + m[1][1] * sinc, - m[1][0] * sinc + m[1][1] * cosc]
    ]
    return rotated
