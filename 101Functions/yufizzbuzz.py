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
