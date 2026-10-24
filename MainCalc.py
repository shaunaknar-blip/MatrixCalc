#this module is the main module that runs the program. It imports the other modules and calls their functions to perform matrix operations.
#for simplicity perposes I have only used two matrices in this program. In the future I will add the ability to use more than two matrices in the operations.
import MatrixCreator
import MatrixAddnSub
print('Welcome to the Matrix Calculator!\n')

matA, mA, nA = MatrixCreator.matrix_create()
matB, mB, nB = MatrixCreator.matrix_create()
#Creating the matrices and storing them along with their dimensions in variables.

print('\nTo perform matrix addition enter \'1\' or the \'+\' symbol.')
print('To perform matrix subtraction enter \'2\' or the \'-\' symbol.\n')

while True: #the main operation performing loop.
    oper = input('Enter your choice: ')
    print()
    if oper == '1' or oper == '+':
        MatrixAddnSub.matrix_addition(matA, mA, nA, matB, mB, nB) #performs addition.
        break
    elif oper == '2' or oper == '-':
        MatrixAddnSub.matrix_subtraction(matA, mA, nA, matB, mB, nB) #performs subtraction.
        break
    else:
        print('Invalid choice')
        continue
