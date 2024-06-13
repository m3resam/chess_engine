def print_table(data):
    text = ''
    colWidths = [0] * len(table_data)
    x = 0
    for i in colWidths:
        for j in data[x]:
            if len(j) > colWidths[x]:
                colWidths[x] = len(j)
        x+=1

    x = 0
    y = 0
    for j in data[0]:
        for i in data:
            print(data[x][y].rjust(colWidths[x]), end=' ')
            x += 1
        print()
        
        x = 0
        y += 1
    
    

    
        

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
