def facRec(x):
    if x<2:
        return 1
    else :
        return x*facRec(x-1)

print(facRec(5))


def facIte(x):
    i = 1
    j = 1
    while i <= x:
        j = j * i
        i = i + 1

    return j
print(facIte(5))