'''
test
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

print(mat)


  print("\n2D matrix is:")
    for i in range(m_rows):
        for j in range(n_col):
            print(matrix[i][j], end=" ")
        print()
'''

class Matrix:
    def __init__(self, name, value): #initialize
        self.name = name
        self.value = value
        self.rows = len(value)
        self.cols = len(value[0]) #checks columns in matrix

    def print(self): #custom print to consol (for spec print style)
        for row in self.value:
            print(row)
    
    def add(self):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            print("Matrices must have the same dimensions")
            return None #check
        
        rows = len(matrix1)
        cols = len(matrix1[0])

        result_add = [[0 for _ in range(cols)] for _ in range(rows)]

        for m in range(rows):
            for n in range(cols):
                result_add[m][n] = matrix1[m][n] + matrix2[m][n] 


    def __str__(self): #official stirng rep
        output = ""
        for row in self.value:
            output += str(row) + "\n"
        return output

    #add - example trixie.plus(alice)
    #multiply
    #times scalar row
    #switch rows

matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix2 = [
    [3, 4, 5, 4],
    [5, 3, 7, 8],
    [9, 10, 25, 12]
]

trixie = Matrix("Matrix 1", matrix1)
print(trixie)         
trixie.print()

'''
user create matrix
def check_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter an integer")

def get_matrix_input():
    name = input("Matrix name: ")
    m_rows = check_int("Enter number of rows: ")
    n_col = check_int("Enter number of columns: ")

    value = []
    print("Input one row at a time (seperate w/ spaces)") #add check for other characters

    for i in range(m_rows):   
        row_input = input("Enter row " + str(i+1) + ": ")
        row = list(map(int, row_input.split()))

        while len(row) != n_col:
            print(f"Please enter exactly [" + str(n_col) + "] values.")
            row_input = input("Enter row " + str(i+1) + ": ")
            row = list(map(int, row_input.split()))

        value.append(row)
    
    return Matrix(name, value)

if __name__ == "__main__":

    print("Create your matrix: ")
    m = get_matrix_input() #usrr input

    print("\nMatrix created:")
    print(m.name)
    for i in range(m.rows):
        for j in range(m.cols):
            print(m.value[i][j], end=" ")
        print()
    print("Rows:" + str(m.rows) + "\nColums:" + str(m.cols))
'''