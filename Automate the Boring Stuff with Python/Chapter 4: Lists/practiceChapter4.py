spam = ['apples', 'bananas', 'tofu', 'cats', 'lions']

for i in spam:
    if i is not spam[-1]:
        print(i, end=', ')
    else:
        print('and ' + i)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0
y = 0
for j in grid:
    for i in grid:
        print(grid[x][y], end=' ')
        x = x + 1
        if x == 9:
            print()
            x = 0
    y = y + 1
    if y == 6:
        break

    

    

    


    
    




    




        
