# Find a square of number without using multiplication and division operator
def findSquare(n):
    sum = 0
    for i in range(0, n):
        sum = sum + n
    return sum


print(findSquare(10))
