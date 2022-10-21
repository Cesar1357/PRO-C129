import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

stars = pd.read_csv('./brightest_stars.csv')
swarfs = pd.read_csv('./brown_dwarfs.csv')
swarfs = swarfs.dropna()
swarfs.Mass = swarfs.Mass.str.replace('[^a-zA-Z0-9]', '').astype('float')

swarfs["Radius"] = swarfs["Radius"]*(0.102763)
swarfs["Mass"] = swarfs["Mass"]*(0.000954588)

swarfs.to_csv("dwarfs_converted.csv",columns=["id","Star_name","Distance","Mass","Radius","Luminosity"])


file1 = './brightest_stars.csv'
file2 = './dwarfs_converted.csv'

d1 = []
d2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p_d1 = d1[1:]
p_d2 = d2[1:]

h = h1+h2

p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
    
fd = pd.DataFrame(p_d)
fd.to_csv("final.csv")

with open("final.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["id","Star_name","Distance","Mass","Radius","Luminosity"])   
    csvwriter.writerows(p_d)





