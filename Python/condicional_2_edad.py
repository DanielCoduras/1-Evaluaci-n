def condicional_2_edad():
    edad=input("cual es tu edad? ")
    if(edad >= 18):
        print "Sala alcoholica"
    else:
        if(edad>=15):
            print "Sala adolescente"
        else:
            print "Sala infantil"

condicional_2_edad()

    
