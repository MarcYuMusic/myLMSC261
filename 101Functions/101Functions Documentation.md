# Marc's Functions Homework
This homework was really straight forward, so I'm just going to list what I did step-by-step. I always do one section of the code first, so I started with this:

```
count = 0

while (count < 100):
    count = count + 1
    print(f"{count}")
```

I had taken this from the Happy Monday example from several weeks go. Then all it was from here is to test if numbers were divisible by 3 and/or 5:

```
count = 0

while (count < 100):
    count = count + 1
    if count%3==0 and count%5==0:
        print("FizzBuzz")
    elif count%3==0:
        print("Fizz")
    elif count%5==0:
        print("Buzz")
    else:
        print(f"{count}")
```

I had a lot more trouble with the group exercise. I just ended up testing a lot of different things. My first misunderstand was that "return" is different from "print". And then I just copied the format of my pyramid code and it worked. Plagiarize yourself!

Group Exercise:

```
def get_power(x, n):
    return x**n

def print_graph(y):
    for i in range(0,3):
        for j in range(y**(2-i)):
            print("#", end="")
        print("\n")
```
