def print_table(tableData):
    colWidths = [0] * len(tableData)

    for line in range(len(tableData)):
        for word in range(len(tableData[line])):
            if colWidths[line] <= len(tableData[line][word]):
                colWidths[line] = len(tableData[line][word])
            else:
                colWidths[line] = colWidths[line]

    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
