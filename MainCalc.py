#this module is the main module that runs the program. It imports the other modules and calls their functions to perform matrix operations.
#for simplicity perposes I have only used two matrices in this program. In the future I will add the ability to use more than two matrices in the operations.
import MatrixCreator
import MatrixOperations
print('Welcome to the Matrix Calculator!')
print('This calculator will peform matrix operations on two matrices that you will create.\n')
print('Let us start by creating the first matrix \'A\'.\n')
matA, mA, nA = MatrixCreator.matrix_create()
print('\nNow create the second matrix \'B\'.\n')
matB, mB, nB = MatrixCreator.matrix_create()
#Creating the matrices and storing them along with their dimensions in variables.


while True: #the main operation performing loop.
    print('\nTo perform matrix addition enter \'1\' or the \'+\' symbol.')
    print('To perform matrix subtraction enter \'2\' or the \'-\' symbol.')
    print('To perform matrix transpose enter \'3\' or the \'T\' symbol.\n')
    oper = input('Enter your choice: ')
    print()
    if oper.strip() == '1' or oper.strip() == '+':
        AnsMat = MatrixOperations.matrix_addition(matA, mA, nA, matB, mB, nB) #performs addition.
    elif oper.strip() == '2' or oper.strip() == '-':
        AnsMat = MatrixOperations.matrix_subtraction(matA, mA, nA, matB, mB, nB) #performs subtraction.
    elif oper.strip() == '3' or (oper.strip()).lower() == 't':
        while True:
            mat_choice = input('Enter the matrix you want to transpose (A or B): ')
            if mat_choice.strip().lower() == 'a':
                AnsMat = MatrixOperations.matrix_transpose(matA, mA, nA) #performs transpose on matrix A.
                break
            elif mat_choice.strip().lower() == 'b':
                AnsMat = MatrixOperations.matrix_transpose(matB, mB, nB) #performs transpose on matrix B.
                break
            else:
                print('Invalid choice. Please enter A or B.')
    else:
        print('Invalid choice')
        continue

    continue_choice = input('Do you want to perform another operation? (Y/N): ')#asks the user if they want to perform another operation on the same matrices or not.
    if continue_choice.strip().lower() == 'y':
        continue
    elif continue_choice.strip().lower() == 'n':
        print('Thank you for using the Matrix Calculator!')
        break
