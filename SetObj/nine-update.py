s = {10,20,30}
s.update([40,50,60],[70,80], range(5))
s.update("Rahul")  # python string is iterable
s.update(10)       #int object is not iterable
print(s)