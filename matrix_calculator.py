def calculate(): 

    number_rows_a = int(input("Enter the number of rows for the first matrix: "))
    number_columns_a = int(input("Enter the number of columns for the first matrix: "))
    number_rows_b = int(input("Enter the number of rows for the second matrix: "))
    number_columns_b = int(input("Enter the number of columns for the second matrix: "))

    assert number_columns_a == number_rows_b

    matrix_a = [[0] * number_columns_a for i in range(number_rows_a)]
    matrix_b = [[0] * number_columns_b for i in range(number_rows_b)]

    for row_index_a in range(number_rows_a):
        for column_index_a in range(number_columns_a):
            prompt_msg = "Insert your entry for row " + str(row_index_a + 1) + " and column " + str(column_index_a + 1) + " of first matrix: "
            entry_a = int(input(prompt_msg))
            matrix_a[row_index_a][column_index_a] = entry_a

    for row_index_b in range(number_rows_b):
        for column_index_b in range(number_columns_b):
            prompt_msg = "Insert your entry for row " + str(row_index_b + 1) + " and column " + str(column_index_b + 1) + " of second matrix: "
            entry_b = int(input(prompt_msg))
            matrix_b[row_index_b][column_index_b] = entry_b

    final_matrix = [[0] * number_columns_b for i in range(number_rows_a)]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                final_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    print(final_matrix)


calculate()


