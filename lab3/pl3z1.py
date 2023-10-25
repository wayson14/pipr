def iter():
    r = range(100)
    b = 0
    for i in r:
        if (i%15 == 0):
            print("fizzbuzz")
        elif (i%5 == 0):
            print("buzz")
        elif (i%3 == 0):
            print("fizz")
        else:
            print(i)

iter()