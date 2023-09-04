print("Salam",1)
x = [1, 7, 2, 6, 12]
n = len(x)

for i in range(n):

    for j in range(0, n - i - 1):

        if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]

print("Sorted array is:", x)
