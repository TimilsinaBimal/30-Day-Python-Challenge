# Write a program to get the sum of n numbers
# Eg: Sum of 123 is 6
# n is user entered value

n = input("Enter the number you want to find sum of: ")
sum = 0
for i in n:
    sum += int(i)
print(f"The sum of {n} is {sum}")
