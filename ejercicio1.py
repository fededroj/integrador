#Ejercicio 1 
def mcd(x,y):
    mcd=1

    if x % y==0:
       return y 

    for k in range(int(y/2),0, -1):
        if x % k == 0 and y % k== 0:
            mcd =k
            break
    return mcd
print('el maximo cumun divisor es : ',mcd(5,10))  