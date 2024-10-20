size = input("Enter Size: ")
for i in range(int(size), 0, -1):
    for j in range(i):
        print(j + 1,end=' ')
    print()
