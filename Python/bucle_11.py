def bucle_11():
    print "*******************"
    print "* SUMA PARES O IMPARES *"
    print "*******************"
    print "Hasta que numero deseas sumar: "
    nfinal=input("numero= ")
    #Definimos una variable para sumar los pares (CONTADORA)
    suma_pares=0  #inicializamos la variable a cero
    #Definimos otra variable para sumar los impares
    suma_impares=0 #inicializamos la variable a cero
    for numero in range(1,nfinal+1):
        if(numero%2==0):
            print str(numero)," es PAR"
            suma_pares=suma_pares+numero
        else:
            print str(numero)," es IMPAR"
            suma_impares=suma_impares+numero
    print "La suma de los numeros pares vale",suma_pares
    print "La suma de los numeros impares vale",suma_impares 

bucle_11()
