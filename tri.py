import random

lst = [random.randint(0, 15) for _ in range(7)]


def tri(lst):
    if len(lst) <= 1:
        return lst
    else:
        return fusion(tri([lst.pop(i) for i in range(round(len(lst) / 2))]), tri(lst))

def fusion(lstA, lstB):
    if lstA == []:
        return lstB
    
    if lstB == []:
        return lstA
    
    if lstA[0] <= lstB[0]:
        return [lstA[0]] + fusion( lstA[1:], lstB)

    else : 
        return [lstB[0]] + fusion( lstA, lstB[1:])

if __name__ == "main":
    print(lst)
    print(tri(lst))
