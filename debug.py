from space2d.Math import *

def do():
    a = [1.0, 0.0]
    print(rotate_vector(a, 3.141/2.0))
    b = [
        [1.0, 0.0],
        [0.0, 1.0]
    ]
    print(rotate_matrix(b, 3.141592653589/2.0))