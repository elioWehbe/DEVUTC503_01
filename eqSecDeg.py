import math
def delta(a,b,c):
   return b*b-4*a*c
def secondDeg(a,b,c):
    delt=delta(a,b,c)
    if delt<0:
        solution=[]
        print("Pas de solution")
    elif delt==0:
        solution=[-b/(2*a)]
    else:
        racine=math.sqrt(delt)
        solution = [(-b + racine) / (2 * a)]
        solution+=[(-b-racine)/(2*a)]

    return solution
print(secondDeg(2,3,-2))