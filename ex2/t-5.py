n = 6  

for i in range(n):
    # Print leading spaces for alignment
    for k in range(i):
        print(" ", end=" ")
    # Print numbers for the current row
    for j in range(i, n):
        print(j + 1, end="   ")
    # Move to the next line after printing each row
    print()
