a=int(input("Ingrese el primer numero (a): " ))
b=float(input("Ingrese el segndo numero (b)"))
c=a+b
if a==b:
    print("igual")
else:
    print("diferente")
print("Tipo de (a) es: ", type(a))
print("Tipo de (b) es: ", type(b))
print("c= ", c)
if type(a)==type(b):
    print("a y b son el mismo")
else: print("a y b son diferentes")