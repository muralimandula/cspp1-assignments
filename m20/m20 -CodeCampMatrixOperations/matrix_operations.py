"""Matrix Operations"""
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
            sum_add = 0
            for k in range(r_2):
                sum_add += int(m_1[i][k])*int(m_2[k][j])
            mul_of_matrices[i] += [sum_add]
    return mul_of_matrices

def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m_1) != len(m_2):  # no.of rows
        print("Error: Matrix shapes invalid for addition")
        return None

    if len(m_1[0]) != len(m_2[0]):   #no.of columns
        print("Error: Matrix shapes invalid for addition")
        return None

    add_of_matrices = []
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
    matrix = []
    for i in range(int(matrix_dimensions[0])):
        # row_list = input().split(" ")
        # matrix.append(row_list)
        matrix += [[int(var) for var in input().split(" ")]]
        if len(matrix[i]) != int(matrix_dimensions[1]):
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    """Main function"""
    # read matrix 1
    m_1 = []
    # matrix_1_dimension = input("Enter no.of rows and columns of matrix 1 : ")
    m_1 = input().split(",")
    # print(m_1)
    matrix_1 = read_matrix(m_1)



    # read matrix 2
    m_2 = []
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
