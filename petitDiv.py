def plusPetit(nombre):
    i=1
    while i<nombre:
        i=i+1
        if nombre%i==0:
         minDiv=i
         break
    return minDiv
print(plusPetit(77))