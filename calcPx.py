def poly(x,list):
    p=0
    if len(list)==0:
        return 1
    else:
       i=0
       while i<list.__len__():
           p += list[i]  * x**i
           i=i+1
    return p

print(poly(2,[1,2,3,4]))
print(poly(3,[1]))