import math
def sumita(x,y):
    print("La suma es ", x+y)
def restita(x,y):
    print("La resta es ", x-y)
def multiNum(x,y):
    print("La multiplicación es ", x*y)
def divNum(x,y):
    print("La división es ", x*y)
def raizNum(x,y):
     print("La raiz de x ",math.pow(x,1/y))
def PotenNum(x,y):
     print("La potencia es ",math.pow(x,y))
def SenNum(x):
   fx= float(x)
   rx= math.radians(fx)
   print ("El seno de x : ", math.sin(rx))

  
  
  
resultado="si"
while resultado!="no":
    print ("""************
Calculadora
************
Menu
1)Suma
2)Resta
3)Multiplicacion
4)Division
5)Raiz
6)Potencia
7)Seno
8) Salir""")
    opcion=int(input("Ingrese su opcion a calcular: "))
    if opcion >= 8 or opcion < 0:
        print("Gracias por usar mi calculadora")
        resultado="no"
         
    else:
        
        if opcion == 7:
          x=int(input("Ingrese el primer numero para calcular: "))
        else:
          x=int(input("Ingrese el primer numero para calcular: "))
          y=int(input("Ingrese el segundo numero para calcular: "))
        
        if opcion==1:
            sumita(x,y)
        elif opcion==2:
            restita(x,y)
        elif opcion==3:
            multiNum(x,y)
        elif opcion==4:
            divNum(x,y)
        elif opcion==5:
           raizNum(x,y)
        elif opcion==6:
           PotenNum(x,y)  
        elif opcion==7:
           SenNum(x)
             
        else:
          print("Gracias por usar mi calculadora")
        resultado=input("Ingrese 'si' o 'no' para realizar un nuevo calculo: ")
