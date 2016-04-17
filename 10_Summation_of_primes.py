#Problem 10 
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return False
count = 0
total = 0
n = 1
while n < 2000000:
    n += 1
    if is_prime(n) != False:
        count += 1
        total += n

print(total)
