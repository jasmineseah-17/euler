#Problem 4
num = 0
for i in range(100000,999*999):
    i = str(i)
    if i[0]==i[5] and i[1]==i[4] and i[2]==i[3]:
        a = 100
        while a<1000:
            if int(i)%a==0 and len(str(int(i)//a))==3:
                num = i            
            a += 1
print(num)
