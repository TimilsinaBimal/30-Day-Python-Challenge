# Write a python program to input centimeter and convert to inch, meter and kilometer

cm = float(input("Enter the vale in Centimeter: "))

# If you need all decial digits remove round function
inValue = round(cm / 2.54, 3)
mValue = round(cm/100, 3)
kmValue = round(cm / 1000, 3)
print(
    f"The equivalent of {cm} is {inValue} inch, {mValue} meter and {kmValue} kilometer")
