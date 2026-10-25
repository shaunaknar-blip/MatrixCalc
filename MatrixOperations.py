#This module contains the functions for performing matrix calculations.
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
    return ansmat

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
    return ansmat

def matrix_transpose(matA, m, n):
    ansmat=[]
    for i in range(n):
        transpose_row = []
        for row in matA:
            transpose_row.append(row[i])
        ansmat.append(transpose_row)
    print("The result of the matrix transpose is:")
    MatrixPrint.matprint(ansmat)
    print()
    return ansmat

'''In all the functions I have returned the answer matrix so that it can be used in future operations if the user wants to perform more than one operation on the same matrices.'''