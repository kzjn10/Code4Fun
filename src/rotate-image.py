# 48
# arr[j][length - i - 1] = matrix[i][j] // Rotate 2D array 90 degree
# def rotate(matrix: list[list[int]]) -> None:
#     length = len(matrix)
#     temp = [8] * length * length
#
#     # Flat rotated 2D array data to 1D array
#     for i in range(length):
#         for j in range(length):
#             temp[j * length + length - i - 1] = matrix[i][j]
#
#     # Convert 1D array to 2D array
#     for i in range(len(temp)):
#         matrix[i // length][i % length] = temp[i]
#
#     print(matrix)

# TC: O(N^2) - Nested loop 2D array to process data
# SC: O(N^2) - Create 1D array of size N^2 to store flattened matrix data

def rotate(matrix: list[list[int]]) -> None:
    length = len(matrix)
    top = 0
    bottom = length - 1

    while top < bottom:
        for col in range(length):
            matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
        top += 1
        bottom -= 1
    for row in range(length):
        for col in range(row + 1, length):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    print(matrix)


# TC: O(N^2) - Nested loop 2D array to process data
# SC: O(1) - No extra array, only use temp variable

# Output: [[7,4,1],[8,5,2],[9,6,3]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
