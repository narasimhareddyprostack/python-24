x = int(input("First Number:"))
y =int(input("Second Number:"))
z  =int(input("Third Number:"))
'''
if x<y and x<z:
    min = x
elif y<z:
    min = y
else:
    min = z
'''
min =x  if x<y and x<z else y if y<z else z 
print(min)