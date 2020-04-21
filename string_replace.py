# program for replacing the string

test_str = "Hello ,   How   are   you?"

# printing original programs
print("The original programs is : " + test_str)

# initializing replace programs
rep_str = input("Enter the  name")

# initializing K
K = 1

#  word replace in String
# using split() + join()
temp = test_str.split(' ')
res = " ".join(temp[: K] + [rep_str] + temp[K + 1:])

# printing result
print("The String after performing replace : " + res)