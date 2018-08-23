def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # pass

    
    r1, c1, r2, c2 = len(m1), len(m1[0]), len(m2), len(m2[0])
    mul_of_matrices = [[] for i in range(r1)]
    if c1 != r2:
        print("Error: Matrix shapes invalid for mult")

    for i in range(r1):
        for j in range(c2):
            sum = 0
            for k in range(r2):
                sum += int(m1[i][k])*int(m2[k][j])
            mul_of_matrices[i] += [sum]
    return mul_of_matrices
            
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    add_of_matrices = [[0 for j in range(len(m1[0]))] for i in range(len(m1))]
    if len(m1)*len(m1[0]) != len(m2)*len(m2[0]):
        print("Error: Matrix shapes invalid for addition")
    for each_row in range(len(m1)):
        for each_column in range(len(m1[0])):
            add_of_matrices[each_row][each_column] = int(m1[each_row][each_column]) + int(m2[each_row][each_column])  
    return add_of_matrices

def read_matrix(matrix_dimensions):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    row = int(matrix_dimensions[0])
    column = int(matrix_dimensions[1])
    length_of_matrix = row*column
    matrix = []
    print("\nEnter", column, "values for each of ", row, " rows below :")
    for each_row in range(row):
        line = input().split()
        matrix.append(line)
    print(matrix, "\n")
    if length_of_matrix == len(matrix)*len(matrix[0]):
        return matrix
    print("Error: Invalid input for the matrix")


    # pass

def main():
    # read matrix 1
    m1=[]
    matrix1_dimension = input("Enter no.of rows and columns of matrix 1 : ")
    m1 = matrix1_dimension.split(",")
    # print(m1)
    matrix1 = read_matrix(m1)



    # read matrix 2
    m2=[]
    matrix2_dimension = input("Enter no.of rows and columns of matrix 2 : ")
    m2 = matrix2_dimension.split(",")
    matrix2 = read_matrix(m2)

    # add matrix 1 and matrix 2

    mat1_mat2 = add_matrix(matrix1, matrix2)
    print("\n",mat1_mat2)

    # multiply matrix 1 and matrix 2
    # pass

    mat1_X_mat2 = mult_matrix(matrix1, matrix2)
    print("\n",mat1_X_mat2)

if __name__ == '__main__':
    main()
