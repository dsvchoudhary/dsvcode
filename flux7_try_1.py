rev = 0
res = 0
for x in range (100, 1000):
    for y in range (100, 1000):
        rev = 0
        prod = x * y
        temp = prod
        revs=str(temp)
        rev=revs[::-1]
        #rev=int(revs)
        # while(prod>0):
        #     num=prod%10
        #     rev=rev*10+num
        #     prod=prod//10
    
        if(revs==rev):
            if(int(revs)>res):
                res=temp
                a = x
                b = y

print (a, "x", b, "=", res)