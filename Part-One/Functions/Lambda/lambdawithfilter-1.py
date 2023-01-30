prices = [40,150,60,180,20]


    
new_Prices = list(filter(lambda n:True if n<100 else False, prices))
print(prices)
print(new_Prices)
