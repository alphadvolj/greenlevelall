def matrix_multiply(A, B):

    if len(A[0]) != len(B):
        raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы.")


    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]


    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

C = matrix_multiply(A, B)
print(C)