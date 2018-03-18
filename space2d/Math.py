import math

def multiply_vector_by_matrix(vector, matrix):
        return [
                vector[0]*matrix[0][0] + vector[1] * matrix[1][0],
                vector[0]*matrix[0][1] + vector[1] * matrix[1][1]
               ]

def rotate_vector(vector, angle):
    return [
            vector[0] * math.cos(angle) + vector[1] * math.sin(angle),
            - vector[0] * math.sin(angle) + vector[1] * math.cos(angle)
    ]

def rotate_matrix(m, a):
    return [
        [m[0][0] * math.cos(a) + m[1][0] * math.sin(a),  - m[0][0] * math.sin(a) + m[1][0] * math.cos(a)],
        [m[0][1] * math.cos(a) + m[1][1] * math.sin(a), - m[0][1] * math.sin(a) + m[1][1] * math.cos(a)]
    ]
