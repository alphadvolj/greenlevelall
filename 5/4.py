matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

transposed_matrix = transpose(matrix)

sum_of_elements = sum(sum(row) for row in transposed_matrix)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nТранспонированная матрица:")
for row in transposed_matrix:
    print(row)

print(f"\nСумма всех элементов транспонированной матрицы: {sum_of_elements}")