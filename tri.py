# tri selection, insertion, bulle(HP) et fusion(Term car récursif)

def triSelection(T):
    N = len(T)
    U=[T[i] for i in range(N)] #U est la copie du tableau T
    for i in range(N):
        min_index = i
        for j in range(i+1, N): #Le nombre d'étape est déterminé car c'est une boucle for le temps d'execution depends de la taille d'entrée du tableau
            if U[j] < U[min_index]:
                min_index = j
        U[i], U[min_index] = U[min_index], U[i] #Permet d'echanger les cases de U[i] et U[min_index]
    return U

def triInsertion(T):
    N = len(T)
    U = T.copy() # U est la copie du tableau T
    for i in range(N): #Le nombre d'étape est déterminé car c'est une boucle for
        reserve = U[i] # met en réserve la case U[i]
        x = i
        while x > 0 and reserve < U[x - 1]: # Le nombre d'étape n'est pas déterminé donc le temps d'execution ne depends pas de la taille d'entrée du tableau
            U[x] = U[x - 1]
            x -= 1
        U[x] = reserve
    return U

def triABulle(T):
    N = len(T)
    U = T.copy()
    for i in range(N): #Le nombre d'étape est déterminé car c'est une boucle for le temps d'execution depends de la taille d'entrée du tableau
        for j in range(0, N-i-1):
            if U[j] > U[j+1]:
                U[j], U[j+1] = U[j+1], U[j]
    return U

def tri_fusion(T):
    N=len(T)
    U=list(T)
    m=N//2
    if N<2:
        return U
    else:
        # Niveau terminale - algorithme récursif
        return fusion(tri_fusion(U[0:m]),tri_fusion(U[m:]))

def fusion(A,B):
    T=[]
    NA=len(A)
    NB=len(B)
    a=0
    b=0
    while a<NA or b<NB:
        if a==NA:
            T.append(B[b])
            b=b+1
        elif b==NB:
            T.append(A[a])
            a=a+1
        else:
            if A[a]>B[b]:
                T.append(B[b])
                b=b+1
            else:
                T.append(A[a])
                a=a+1
    return T

# Test
def main():
    tab1=[67,12,7,28,42]
    tab2=[4]
    tab3=[7,7,7,7,2]
    tab1=triInsertion(tab1)
    tab2=triInsertion(tab2)
    tab3=triInsertion(tab3)
    assert tab1==[7,12,28,42,67]
    assert tab2==[4]
    assert tab3==[2,7,7,7,7]
    tab1=[67,12,7,28,42]
    tab2=[4]
    tab3=[7,7,7,7,2]
    tab1=triSelection(tab1)
    tab2=triSelection(tab2)
    tab3=triSelection(tab3)
    assert tab1==[7,12,28,42,67]
    assert tab2==[4]
    assert tab3==[2,7,7,7,7]
    tab1=[67,12,7,28,42]
    tab2=[4]
    tab3=[7,7,7,7,2]
    tab1=triABulle(tab1)
    tab2=triABulle(tab2)
    tab3=triABulle(tab3)
    assert tab1==[7,12,28,42,67]
    assert tab2==[4]
    assert tab3==[2,7,7,7,7]
    tab1=[67,12,7,28,42]
    tab2=[4]
    tab3=[7,7,7,7,2]
    tab1=tri_fusion(tab1)
    tab2=tri_fusion(tab2)
    tab3=tri_fusion(tab3)
    assert tab1==[7,12,28,42,67]
    assert tab2==[4]
    assert tab3==[2,7,7,7,7]
    print("OK")

if __name__ == "__main__":
    main()
