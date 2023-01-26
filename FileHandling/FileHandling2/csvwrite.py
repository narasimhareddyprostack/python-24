import csv
list1 =['id','name','sal']
list2 = [101,'rahul', 45000]

f = open("sal.csv","w")
csvobj = csv.writer(f)
csvobj.writerow(list1)
csvobj.writerow(list2)
f.close()