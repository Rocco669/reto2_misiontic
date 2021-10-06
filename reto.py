def sumar(n1,n2):
    return n1+n2

print("calculadora ejemplo")
print()
print("1). SUMAR")


op=int(input("digite una opcion: "))
n1=int(input("digite el numero: "))
n2=int(input("Digite el numero 2: "))
res=None
if op==1:
    res=sumar(n1,n2)
    
print("el resultado es: ", res)
print("este es un cambio que hizo om5")