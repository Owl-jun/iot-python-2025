def printer() :
    while True :
        string = (yield) ** 2
        print(f'{string}')
        
            
        
        


p = printer()

next(p)
p.send(5)




