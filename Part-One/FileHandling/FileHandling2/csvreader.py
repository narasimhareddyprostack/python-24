#importing csv module to work in csv files

import csv
import sys
f = open("data.csv", "r")

#get the CSV reader object
reader  = csv.reader(f)
for line in reader:
    for word in line:
        print(word,"\t")
        