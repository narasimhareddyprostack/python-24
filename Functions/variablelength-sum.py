def add(*a):
    #print(a) tuple
    total = 0
    for x in a:
        total = total + x
    
    print(total)
    

add()
add(10)
add(10,20)
add(10,20,30)
add(10,20,30,40)