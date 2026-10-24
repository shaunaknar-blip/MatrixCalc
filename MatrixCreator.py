def matrix_create(mat_list):
    while True:
        try:
            n = int(input("Enter the number of columns: "))
            m = int(input("Enter the number of rows: "))
            break
        except ValueError:
            print("Please enter valid integers.")
            continue

    for i in range(1,m+1):
        row = []
        for j in range(1,n+1):
            while True:
                try:
                    value = float(input(f"Enter the value for {i}x{j}: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Please enter a valid number.")
        mat_list.append(row)

    max_width = max(len(str(j)) for row in mat_list for j in row)

    for i in range(m):
        row = mat_list[i]
        print("|", end=' ')
        for j in row:
            print(f"{j:>{max_width}}", end=' ')
        print("|")