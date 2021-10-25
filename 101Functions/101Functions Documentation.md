# Marc's Functions Homework
This homework was really straight forward, so I'm just going to list what I did step-by-step. I always do one section of the code first, so I started with this:

count = 0

while (count < 100):
    count = count + 1
    print(f"{count}")

I had taken this from the Happy Monday example from several weeks go. Then all it was from here is to test if numbers were divisible by 3 and/or 5:

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