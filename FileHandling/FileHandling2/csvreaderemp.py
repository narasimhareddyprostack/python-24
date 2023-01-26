import csv

f = open("data.csv","r")
reader = csv.reader(f)
for line in reader:
    for word in line:
        print(word, "\t", end="" )
    print()
        