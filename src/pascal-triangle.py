# 118. Pascal's triangle
def pascal_triangle(num_rows: int):
    result = []
    # Start at 1 to num rows + 1 to avoid first list empty
    for i in range(1, num_rows + 1):
        # Create new array with default value 1
        row = [1] * i
        # Loop j in range i
        for j in range(i):
            # Calculator item difference first and last
            if 0 < j < (i - 1):
                # Get position of last row and top left + top right
                row[j]= result[i - 2][j - 1] + result[i - 2][j]
        # Add row
        result.append(row)
    return result

#Brute force
#TC: O(N^2) Nested loop
#SC: O(N^2) Matrix n x m
print(pascal_triangle(5))