for i in range(0, 6):
    for j in range(0, 6-i-1):
        print(end="")
    for j in range(0, i+1):
        print("*", end=" ")
    print()


# def pattern(n):
#     for i in range(1, n + 1):
#         k = i + 1 if (i % 2 != 0) else i

#         for g in range(k, n):
#             if g >= k:
#                 print(end=" ")
#         for j in range(0, k):
#             if j == k-1:
#                 print(" * ")
#             else:
#                 print(" * ", end="")

# pattern(4)
