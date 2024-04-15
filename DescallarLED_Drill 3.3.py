N = int(input("Enter N:"))
a = 2
while N != 0:
    for i in range (2, a):
        if a %i == 0:
            break
    else:
        print (a, end = " ")
        N -= 1
    a += 1
