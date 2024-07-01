r = int(input('row:'))
c = int(input('collumn:'))
middle_column = (c + 1) // 2
middle_row = (r + 1) // 2
for r in range(1,middle_row+1):
    for c in range(1,c+1):
        if r <= middle_row:
            if (c == middle_column + r) or (c == middle_column - r):
                print('x',end='')
            elif (r == middle_row-1) and (c == middle_column):
                print('1',end='')
            elif (c == middle_column-1) and (r == middle_row):
                print('1',end='')
            elif (c == middle_column+1) and (r == middle_row):
                print('1',end='')
            else:
                print('a',end='')
    print()
for r in range(middle_row-1,0,-1):
    for c in range(1,c+1):
        if r < middle_row:
            if (c == middle_column + r) or (c == middle_column - r):
                print('x',end='')
            elif (r == middle_row-1) and (c == middle_column):
                print('1',end='')
            else:
                print('a',end='')
    print()