def get_power(x, n):
    return x**n

def print_graph(y):
    for i in range(0,3):
        for j in range(y**(2-i)):
            print("#", end="")
        print("\n")
