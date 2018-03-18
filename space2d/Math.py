def multiply_vector_by_matrix(vector, matrix):
        return [
                vector[0]*matrix[0][0] + vector[1] * matrix[1][0],
                vector[0]*matrix[0][1] + vector[1] * matrix[1][1]
               ]

