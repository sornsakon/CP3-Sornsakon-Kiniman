step = int(input("Enter the number of pyramid steps : "))
for i in range(step):
    j = 1+2*i
    print(" "*(step-i)+"*"*(j))