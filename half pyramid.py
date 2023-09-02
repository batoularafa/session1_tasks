num =  int(input("enter number from 1-8:"))
if num > 8 or num < 1 :
    num =  int(input("enter number from 1-8:"))
space = num

for j in range(0,num):
    for y in range(space, 1, -1):
        print(" ", end = "")
    space -= 1
    
    for x in range(0, j+1):
        print("#", end="")
    print("  ",end="")

    for i in range(0,j+1):
         print("#", end="")

    print("")
    