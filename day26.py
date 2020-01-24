# The temperature recorded at 8AM is n deg Celcius.
# What is the equivalent of this temperature in degrees Fahrenheit?

# n is user enteres value.

n = int(input("Enter the temperature in degree Celcius: "))
result = (n * 9/5) + 32
print(f"The temperature {n} degree Celcius in degree Fahrenheit is: {result}")
