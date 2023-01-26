def outer():
    def inner():
        print("Inner function")
        
    return inner


x = outer()
print(x())