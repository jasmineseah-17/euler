#Problem 2
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
count = 0
x = 2
index = 0
while index<4000000:
    index = fib(x)
    if index%2==0:
        count += fib(x)
    x += 1
print(count)
