def outer():
        
    def inner():
        print('inner function')
    
    return inner

inner = outer()
inner()
inner()