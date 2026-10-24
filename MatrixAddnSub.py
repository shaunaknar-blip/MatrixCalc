#This module contains the functions for adding and subtracting matrices.
import MatrixPrint

def matrix_addition(matA, mA, nA, matB, mB, nB):
    ansmat = []
    if mA != mB or nA != nB:
        print("Matrices must have the same dimensions for addition.")
    else:
        for rowA, rowB in zip(matA, matB):
            result_row = [a + b for a, b in zip(rowA, rowB)]
            ansmat.append(result_row)
        print("The result of the matrix addition is:")
        MatrixPrint.matprint(ansmat)
        print()

def matrix_subtraction(matA, mA, nA, matB, mB, nB):
    ansmat = []
    if mA != mB or nA != nB:
        print("Matrices must have the same dimensions for subtraction.")
    else:
        for rowA, rowB in zip(matA, matB):
            result_row = [a - b for a, b in zip(rowA, rowB)]
            ansmat.append(result_row)
        print("The result of the matrix subtraction is:")
        MatrixPrint.matprint(ansmat)
        print()

'''In both these functions I have returned the result even after printing it, so that it can be used in other functions if needed.
The ability of which will be added in future updates of this program.'''