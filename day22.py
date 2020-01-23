# Write a python program to find if a given year is a leap year or not
year = int(input("Enter the year you want to Check: "))
if year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
