a = int(input("Enter First Number:"))
b= int(input("Enter Second Number:"))

def maxValue(a,b):
    return a if a>b else b
    
print(maxValue(a,b))