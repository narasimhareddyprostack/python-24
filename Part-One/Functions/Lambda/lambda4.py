a = int(input("Enter First Number:"))
b= int(input("Enter Second Number:"))

maxValue = lambda a,b : a if a>b else b
    
print(maxValue(a,b))