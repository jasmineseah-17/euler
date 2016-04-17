#Problem 5
x = 19*20
while True:
    count = 0
    for i in range(3,21):
        if x%i== 0:
            count += 1
    if count == 18:
        print(x)
        break
    else:
        x += 20*19
