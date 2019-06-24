import numpy as np

n = int(input("Enter the odd order of matrix\n"))
if (n % 2 != 0):
    print("Yoy should enter an odd number:")
    n = int(input("Please enter odd number"))

a = np.zeros((n, n), type(int))
i = 0
j = n // 2
a[i][j] = 1
for k in range(2, n * n + 1):
    i = i - 1
    j = j + 1

    if (i == -1 and j != n):
        i = n - 1
        if (a[i][j] != 0):
            i = 1
            j -= 1
    if (j == n and i != -1):
        j = 0
        if (a[i][j] != 0):
            j = n - 1
            i += 2
    if (i == -1 and j == n):
        i = n - 1
        j = 0
        if (a[i][j] != 0):
            i = 1
            j = n - 1
    if (a[i][j] != 0):
        i += 2
        j -= 1
    a[i][j] = k

print((a))