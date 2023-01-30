a = int(input("Enter First Number:"))
b= int(input("Enter Second Number:"))

def maxValue(a,b):
    if a>b:
        return a
    else:
        return b
    
print(maxValue(a,b))