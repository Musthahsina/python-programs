# import csv
# with open('data-.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
'''dictionary format'''
import csv

'''read'''
# import csv
# with open('data2.csv', 'w') as csvfile:
#     filenames=['Firstname','Lastname','Age','Year']
#     writer=csv.DictWriter(csvfile,fieldnames=filenames)
#     writer.writeheader()
#
#     writer.writerow({"Firstname":"musthahsina","Lastname":"alukkal","Age":26,"Year":1997})
#     csvfile.close()

# with open("data2.csv",'r') as file:
#     csvfile = csv.DictReader(file)
#     for row in csvfile:
#         print(row)

'''read csv as list'''
import csv
with open('data-.csv', 'r') as data:
    for line in csv.reader(data):
        print(line)
