import time 

while True:
 print ("## Elija la operacion a realizar ##") 
 print("1. Suma")
 print("2. Resta")
 print("3. Multiplicar")
 print("4. Dividir")
 print("5. Salir")

 operacion= int (input("#ingrrese la opcion deseada#\n "))
 if operacion == 5 :
  print("cerrando el programa  bye ")
  time.sleep(0.3)
  break
  
 if operacion < 1 or operacion > 5:
        print("Elija solo las opciones disponibles\n")
        time.sleep(0.6)
        continue
    
 numero1 = int(input("ingrese el primer numero: \n"))
 numero2 = int(input("ingrese el segundo numero: \n"))

 if operacion == 1 :
  print("el resultado de la suma es:\n " +str( numero1 + numero2))
 elif operacion == 2:
  print("el resultado de la resta es:\n " + str( numero1 - numero2))
 elif operacion == 3:
  print("el resultado de la multiplicacion es:\n " + str( numero1 * numero2)) 
 elif operacion == 4:
   if numero2 == 0 :
     print ("no se puede dividir entre cero\n")
   else:
     print ("la divicion es:\n "+ str (numero1 / numero2 ))  