N = int(input("Enter an integer:"))

for i in range (0,N):
    for j in range (0,2*N+1):
        if (j==2*N or j==N+1 or j<N):
            print("*",end="")
        elif ((i==0 or i==N-1) and j!=N):
            print("*",end="")
        else:
            print(" ",end="")
    print("")