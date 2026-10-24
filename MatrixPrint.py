#this function prints a matrix in a formatted way

def matprint(mat_list):
    max_width = max(len(str(item)) for row in mat_list for item in row) 
    #this finds the maximum width of any item in the matrix for formatting

    for row in mat_list:
        print("|", end=' ')
        for j in row:
            print(f"{j:>{max_width}}", end=' ')#this prints each item in the row with right alignment based on the maximum width
        print("|")
