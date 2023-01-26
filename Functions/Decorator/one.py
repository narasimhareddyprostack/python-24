def addPosition(func):
    def greet(name):
        if name =="Modi":
            return "PM"+name
        else:
            return func(name)
    return greet

@addPosition
def wish(name):
    return "Hello:"+name


print(wish("Rahul"))
print(wish("Sonia"))
print(wish("Modi"))