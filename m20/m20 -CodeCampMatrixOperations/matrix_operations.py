def mult_matrix(m_1, m_2):
    '''
        check if the matrix_1 columns = matrix_2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # pass

    r_1, c_1, r_2, c_2 = len(m_1), len(m_1[0]), len(m_2), len(m_2[0])
    mul_of_matrices = [[] for i in range(r_1)]
    if c_1 != r_2:
        print("Error: Matrix shapes invalid for mult")
        return None

    for i in range(r_1):
        for j in range(c_2):
            sum = 0
            for k in range(r_2):
                sum += int(m_1[i][k])*int(m_2[k][j])
            mul_of_matrices[i] += [sum]
    return mul_of_matrices

def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    """My code"""
    # add_of_matrices = [[0 for j in range(len(m_1[0]))] for i in range(len(m_1))]
    # # print(add_of_matrices)
    # if len(m_1)*len(m_1[0]) != len(m_2)*len(m_2[0]):
    #     print("Error: Matrix shapes invalid for addition")
    #     return None
    # for row in range(len(m_1)):
    #     for column in range(len(m_1[0])):
    #         add_of_matrices[row][column] = int(m_1[row][column]) + int(m_2[row][column])
    # return add_of_matrices

    """Code by GS"""
    if len(m_1) != len(m_2):  # no.of rows
       print("Error: Matrix shapes invalid for addition")
       return None

    if len(m_1[0]) != len(m_2[0]):   #no.of columns
       print("Error: Matrix shapes invalid for addition")
       return None

    # mat_add = [[0 for j in range(len(m_1[0]))] for i in range(len(m_1))]
    # for i, mat in enumerate(m_1):
    #    for j, _ in enumerate(mat):
    #        mat_add[i][j] = int(m_1[i][j]) + int(m_2[i][j])
    # return mat_add[:]
    add_of_matrices =[]
    for row in range(len(m_1)):
        row_list = []
        for column in range(len(m_1[0])):
            row_list.append(int(m_1[row][column]) + int(m_2[row][column]))
        add_of_matrices.append(row_list)
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
    # print("\nEnter", column, "values for each of ", row, " rows below :")
    for each_row in range(row):
        line = input().split()
        matrix.append(line)
    # print(matrix, "\n")
    if length_of_matrix == len(matrix)*len(matrix[0]):
        return matrix
    print("Error: Invalid input for the matrix")
    return None


    # pass

def main():
    # read matrix 1
    m_1=[]
    # matrix_1_dimension = input("Enter no.of rows and columns of matrix 1 : ")
    m_1 = input().split(",")
    # print(m_1)
    matrix_1 = read_matrix(m_1)



    # read matrix 2
    m_2=[]
    # matrix_2_dimension = input("Enter no.of rows and columns of matrix 2 : ")
    m_2 = input().split(",")
    matrix_2 = read_matrix(m_2)

 
    if matrix_1 is not None and matrix_2 is not None:
       print(add_matrix(matrix_1, matrix_2))
       print(mult_matrix(matrix_1, matrix_2))
    # add matrix 1 and matrix 2
    # multiply matrix 1 and matrix 2
if __name__ == '__main__':
    main()
