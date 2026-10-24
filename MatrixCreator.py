#this file contains the function for creating a matrix and returning it along with its dimensions

import MatrixPrint

def matrix_create():
    mat_list = [] #this is the list that will hold the matrix
    while True:
        try:
            n = int(input("Enter the number of columns: "))
            m = int(input("Enter the number of rows: "))
            if n <= 0 or m <= 0:
                print("Please enter positive integers for the number of rows and columns.")
                continue
            break
        except ValueError:
            print("Please enter valid integers.")
            continue
    print()
    for i in range(1,m+1):
        row = [] #this is the list that will hold the current row of the matrix
        for j in range(1,n+1): #this loop will iterate through the number of columns and prompt the user to enter a value for each position in the current row
            while True:
                try:
                    value = float(input(f"Enter the value for {i}x{j}: ")) #this prompts the user to enter a value for the current position in the matrix
                    row.append(value)
                    break
                except ValueError:
                    print("Please enter a valid number.")
        mat_list.append(row)
    print("\nThe matrix you entered is:")
    MatrixPrint.matprint(mat_list)
    print()
    return mat_list, m, n
matrix_create()
'''I have returned the matrix along with the number of rows and columns so that they can be used in other functions without having to recalculate them.'''