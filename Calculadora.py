import math
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
        print("gracias por usar mi calculadora")
        resultado="no"
    else:
        x=int(input("Ingrese el primer numero para calcular: "))
        y=int(input("Ingrese el segundo numero para calcular: "))
        if opcion==1:
            print("la suma es ", x+y)
        elif opcion==2:
            print("la resta es ", x-y)
        elif opcion==3:
            print("la multiplicacion es ", x*y)
        elif opcion==4:
            print("la division es ",x/y)
        elif opcion==5:
            print("la raiz de x ",math.pow(x,1/y))
        elif opcion==6:
            print("la potencia es ",math.pow(x,y))
        elif opcion==7:
            fx= float(x)
            fy= float(y)
            rx= math.radians(fx)
            ry= math.radians(fy)
            print ("El seno de x : ", math.sin(rx))
            print ("El seno de y : ", math.sin(ry))
             
        else:
          print("gracias por usar mi calculadora dentro del sw")
        resultado=input("ingrese 'si' o 'no' para realizar un nuevo calculo: ")
