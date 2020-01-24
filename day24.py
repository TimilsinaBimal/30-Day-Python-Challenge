# If Julius has j books and Nancy has n. How many books do they have altogether?
# Convert and print as roman number.
# j and n are user entered value

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num_to_roman(num):
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman


jBook = int(input("Enter the Julius Book Count: "))
nBook = int(input("Enter the Nancy Book Count: "))
total = jBook + nBook
print(f"The Value {total} in Roman is: {num_to_roman(total)}")
