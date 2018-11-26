def piramide():
    y = input  ("Indica de que altura deseas tu piramide: ")
    for i in range (0,y):
        for i in range (0,i+1,1):
            print "*",
        print ""
        
        
piramide()
