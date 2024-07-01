for r in range(0,6):
    for c in range(0,11):
        if r==c:
            print(r+1,end=' ')
        elif c==r+2 and r<5:
            print(r+2,end=' ')
        elif c==r+4 and r<4:
            print(r+3,end=' ')
        elif c==r+6 and r<3:
            print(r+4,end=' ')
        elif c==r+8 and r<2:
            print(r+5,end=' ')
        elif c==r+10 and r<1:
            print(r+6,end=' ')

        else:
            print(end=' ')
    print()

# for r in range(0,6):
#     for c in range(0,11):
#         if c==r+2:
#             print(r+1,end='')
#         else:
#             print(end=' ')
#     print()