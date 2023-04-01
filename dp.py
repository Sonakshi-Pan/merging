import csv

d1 = []
d2 = []
with open("bright_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        d1.append(row)

with open("dwarf_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        d2.append(row)

h1 = d1[0]
star_d1 = d1[1:]
h2 = d2[0]
star_d2 = d2[1:]

h = h1+h2

star_d =[]

for index,datarow in enumerate(star_d1):
    star_d.append(star_d1[index]+star_d2[index])

with open("final2.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(star_d)    