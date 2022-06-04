def operation(operation1, num_rows=9, num_columns=9):
    for i in range(num_rows):
        table = []
        for j in range(num_columns):
            table += [operation1(i+1, j+1)]
        print(*table, sep="\t")


operation(lambda x, y: x * y)
print("\n")

operation(lambda x, y: x * y, 5)
print("\n")

operation(lambda x, y: x ** y, 4, 4)
print("\n")

operation(lambda x, y: x + y, 5, 5)
print("\n")