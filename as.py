import csv
data=[]
with open("bright_stars.csv","r")as f:
    csvreader=csv.reader(f)

    for row in csvreader:
        data.append(row)

headers=data[0]
stars_data=data[1:]
for datapoint in stars_data:
    datapoint[2]=datapoint[2].lower()
stars_data.sort(key=lambda stars_data:stars_data[2]) 
with open("ads.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)   

with open('bright_stars.csv')as input,open('dwarf_stars.csv','w',newline='')as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row ):
            writer.writerow(row)