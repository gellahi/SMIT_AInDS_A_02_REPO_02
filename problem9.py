size = input("Enter Size: ")
for i in range(1, int(size) + 1):
    for j in range(i, 0, -1):
        print(j,end=' ')
    print()
