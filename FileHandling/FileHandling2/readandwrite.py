import csv

f1 = open("data.csv", "r")
f2 = open("newData.csv","w")

reader = csv.reader(f1)
csvWriter = csv.writer(f2)
for line in reader:
    csvWriter.writerow(line)
    
f1.close()

f2.close()
    
    