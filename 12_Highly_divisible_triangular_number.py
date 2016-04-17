#Probelm 12
arr = [1]
index = 1
count = 0
while count < 501:
    count = 0
    x = arr[index-1]+index+1
    print("x", x)
    for i in range(1,int(x**(0.5))+1):
        if x%i ==0:
            count += 1
            if i*i != x:
                count+=1
    arr.append(x)
    index +=1
print(x)
