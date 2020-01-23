# Write a python program to convert integer values into binary

binary = []


def int_to_binary(num):
    if num < 2:
        binary.append(num)
    elif num % 2 == 0:
        binary.append(0)
        int_to_binary(num//2)
    else:
        binary.append(num % 2)
        int_to_binary(num // 2)
    result = ""
    for i in binary[::-1]:
        result += f"{i}"
    return int(result)


decimal = int(input("Enter the Decimal Number: "))
print(f"The binary of {decimal} is {int_to_binary(decimal)}")
