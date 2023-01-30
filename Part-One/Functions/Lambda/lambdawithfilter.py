prices = [40,150,60,180,20]

def belowHundred(n):
    if n<100:
        return True
    else:
        return False
    
new_Prices = list(filter(belowHundred, prices))
print(prices)
print(new_Prices)