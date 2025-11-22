'''
Matrix: two dim ray of numbers, m rows and n columns, entries are real numbers

Base Assignment
    Matrix class must have print, plus, times, scalarTimesRow, switchRows, linearCombRos, rowreduce, and invert

'''

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

print(mat)

m_rows = int(input("Input the number of rows: "))
n_col = int(input("Input the number of columns: "))

matrix = []
print("Input one row at a time (seperate w/ spaces)")

for i in range(m_rows):   
    row_input = input("Enter row " + str(i+1) + ": ")
    row = list(map(int, row_input.split()))

    while len(row) != n_col:
        print(f"Please enter exactly " + str(n_col) + " values.")
        row_input = input(f"Enter row {i+1}: ")
        row = list(map(int, row_input.split()))

    matrix.append(row)


print("\n2D matrix is:")
for i in range(m_rows):
    for j in range(n_col):
        print(matrix[i][j], end=" ")
    print()