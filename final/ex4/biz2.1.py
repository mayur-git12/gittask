for r in range(0,9):
    for c in range(0,9):
        if (r==0 or r==8) and c%2!=0:
            print('*',end='')
        elif (c==0 or c==8) and r%2!=0:
            print('*',end='')
        elif r==0 and c%2==0:
            print(c+1,end='')
        elif c==0 and r%2==0:
            print(r+1,end='')
        elif c==8 and r%2==0 and r>0:
            print(9-r,end='')
        elif r==8 and c%2==0 and c>1 and c<7:
            print(9-c,end='')

        else:
            print(end=' ')
    print()
        