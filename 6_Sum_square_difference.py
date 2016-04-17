#Problem 6
sq = 0
total = 0
for i in range(1,101):
    sq += i**2
    total += i
print(total**2 - sq)
