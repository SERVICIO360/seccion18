cantidad=0
menor=0
n=int(input("INGRESE CANTIDAD DE PERSONAS"))
for e in range(n):
   edad=int(input("INGRESE EDAD"))
   if(edad>17):
       cantidad=cantidad+1
   else: 
      menor=menor+1 
print("LA CANTIDAD DE PERSONAS MAYORES",cantidad)
print("LA CANTIDAD DE MENORES",menor)