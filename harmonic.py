#  program to find the sum of harmonic series

def sum(n):
    i = 1
    s = 0.0
    for i in range(1, n + 1):
        s = s + 1 / i
    return s


# Driver Code
n = int(input("Enter number: "))
print("Sum is", round(sum(n), 4))