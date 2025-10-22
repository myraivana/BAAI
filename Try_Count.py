# 1. Try to print count 1 - 5
#for i in range(1, 6):
#    print(f"Count: {i}")

# 2. Try to print count 1 - 5 (in 1 line, no new line)
#for i in range(1, 6):
#    print(f"Count: {i}", end=" ")

# 3. Try to print count 1 - 5 (put commas, but not after 5)
#for i in range(1, 6):
#    print(f"Count: {i}", end=", " if i < 5 else "\n")
#or
#for i in range(1,6):
#    if i < 5:
#        print(f"Count: {i},", end=" ")
#    else:
#        print(f"Count: {i}")

# 4. Try to print count 1 - 5 (put "Output: " in the beginning)
print("Output:", end=" ")
for i in range(1,6):
    if i < 5:
        print(f"Count: {i},", end=" ")
    else:
        print(f"Count: {i}")