def piramide_invertida():
    y = input ("Dame y: ")
    for i in range (y,0):
        for i in range (0,i+1,1):
            print "*",
        print ""


piramide_invertida()
