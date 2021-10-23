stacks = int(input("How tall should the pyramid be? "))

for i in range(stacks):
    for j in range(stacks-i):
        print(" ", end="")
    for j in range(i+1):
        print("#", end="")
    print("\n")
