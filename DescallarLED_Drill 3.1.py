N = int(input("Enter N: "))
print (N)

if N>0:
    for i in range(N):
        for j in range(N):
             if j == i :
                print("*", end="")
             elif j == 0:
                print("*", end="")
             elif i == N-1:
                print("*", end="")
             else:
                print(" ", end="")
        print("")