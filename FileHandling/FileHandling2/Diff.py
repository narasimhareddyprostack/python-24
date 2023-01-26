f1 = open("one.txt",'w')
f2 = open("two.txt","a")

f1.write("Welcome to Python World")
f2.write("Welcome to Python World")

f1.close()
f2.close()