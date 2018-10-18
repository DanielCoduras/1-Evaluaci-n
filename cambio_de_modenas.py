def cambio_de_monedas():
    euros=input("Introduce una cantidad: ")
    respuesta=raw_input(" A que moneda deseas cambiar?")
    if(respuesta == "dolares"):
        print "Sean "+ str(euros*1.15)+ " dolares"
    if(respuesta == "libras"):
        print "Sean "+ str(euros*0.88)+ " libras"
       
    
cambio_de_monedas()
    

        
    
