# A floppy disk shows f bytes of free and u bytes of used.
# If you delete a file of size o bytes and create a new file of size n bytes,
# how many free bytes will the floppy disk have?
# f,u,o,n are the user-entered value

f = int(input("Enter the size(bytes) of free space on disk: "))
u = int(input("Enter the size(bytes) of Used space on disk: "))
n = int(input("Enter the size(bytes) of added file on disk: "))
o = int(input("Enter the size(bytes) of deleted file on disk: "))

freeSize = f - n + o
if f + o < n:
    print("ERROR: The added file has greater in size than free space available")

print(f"The final free size on disk is: {freeSize}")
