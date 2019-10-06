# A floppy disk shows f bytes of free and u bytes of used.
# If you delete a file of size o bytes and create a new file of size n bytes,
# how many free bytes will the floppy disk have?
# f,u,o,n are the user-entered value

f = int(input("Enter the size(bytes) of free space on disk: "))
u = int(input("Enter the size(bytes) of Used space on disk: "))
o = int(input("Enter the size(bytes) of added file on disk: "))
n = int(input("Enter the size(bytes) of deleted file on disk: "))

freeSize = f - o + n
if f+n < o:
    print("The file cannot be added(free size is less tha file added size)")

print(f"The final free size on disk is: {freeSize}")
