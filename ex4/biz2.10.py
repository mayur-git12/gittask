for r in range(0,5):
    for c in range(0,9):
        if r==c and r%2==0:
            print('A',end='')
        elif r==c and r%2!=0:
            print('a',end='')
        elif c==r+2 and r%2==0 and c<5 and r<3:
            print('B',end='')
        elif c==r+2 and r%2!=0 and c<6 and r<4:
            print('b',end='')
        elif c==r+4 and r%2==0 and c<7 and r<3:
            print('C',end='')
        elif c==r+4 and r%2!=0 and c<6 and r<2:
            print('c',end='')
        elif c==r+6 and r%2==0 and c<7 and r<1:
            print('D',end='')
        elif c==r+6 and r%2!=0 and c<8 and r<2:
            print('d',end='')
        elif r==0 and c==8:
            print('E',end='')

        else:
            print(end=' ')
    print()
