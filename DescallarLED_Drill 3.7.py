N = int(input("Please input side length of diamond: "))
if N > 0:             
    for i in range(N):
        for s in range (N - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()
    for i in range(N, 0, -1):
        for s in range (N - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()