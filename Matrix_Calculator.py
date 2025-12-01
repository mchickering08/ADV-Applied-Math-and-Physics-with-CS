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
        for row in self.value: #for every row in the matrix
            print(row)
    
    def plus(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Matrices must have the same dimensions")
            return None
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.value[i][j] + other.value[i][j])
            result.append(row)
        
        return Matrix(self.name + "_plus_" + other.name, result)

    def times(self, other):
        # Check dimensions: self.cols must equal other.rows
        if self.cols != other.rows:
            print("Number of columns in the first matrix must equal the number of rows in the second matrix")
            return None

        result = [] #create empty result
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.value[i][k] * other.value[k][j]
                row.append(total)
            result.append(row)

        return Matrix(self.name + "_times_" + other.name, result)


    def __str__(self): #official stirng rep
        output = ""
        for row in self.value:
            output += str(row) + "\n"
        return output

    #add - example trixie.plus(alice)
    #multiply
    #times scalar row
    #switch rows

trixie = Matrix("A", [[1, 2], [3, 4]])
alice = Matrix("B", [[5, 6], [7, 8]])

trixie.print()
print("\n")
print(trixie.plus(alice)) 
print(trixie.times(alice))

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