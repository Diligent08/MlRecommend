#----------------------------------@@@TECH DIVAS@@@------------------------
#Importing all necessary libraries
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')
import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
#Defining a function to convert list items to string
def listToString(s):
    # initialize an empty string
    stry = ""

    # traverse in the string
    for ele in s:
        stry += ele
    return stry
#Definig a  function to generate random number between 'start' and 'end'
# for 'num' no.of iterations
def Rand(start, end, num):
    review1 = []

    for j in range(num):
        review1.append(random.randint(start, end))
    return review1
#Loading the DATASET in required format.Here format used is csv files.File
#is loaded using the pandas library

train_data=pd.read_csv('skroutz_laptops.csv' ,sep=',', encoding='latin-1')

#CLEANING THE DATASET
#Converting textual values to numerical values
for i in train_data['Weight']:
    j = i[:-2]
    train_data.replace(i,j,inplace=True)
rating=Rand(1,5,1303)
train_data['rating']=rating
#Converting different company names to numerical values
Company={'Dell':1,'Apple':2,'Asus':3,'Acer':4,'Lenovo':5,'HP':6,'Chuwi':7,'MSI':8,'Microsoft':9,'Huawei':10,'Toshiba':11,'Mediacom':12,'Fujitsu':13,'Google':14,'Samsung':15,'Razer':16,'Vero':17,'Xiaomi':18,'LG':19}
train_data.head()
train_data.Company = [Company[item] for item in train_data.Company]
train_data['Company'].value_counts().sort_index().plot.bar()
Ram={'2GB':2,'4GB':4,'6GB':6,'8GB':8,'12GB':12,'16GB':16,'24GB':24,'32GB':32,'64GB':64}

train_data.Ram = [Ram[item] for item in train_data.Ram]

TypeName={'Ultrabook':0,'Notebook':1,'Gaming':2,'2 in 1 Convertible':3,'Workstation':4,'Netbook':5}
train_data.TypeName = [TypeName[item] for item in train_data.TypeName]
OpSys={'No OS':0,'Windows 10':1,'Linux':2,'macOS':3,'Windows 7':4,'Mac OS X':5,'Windows 10 S':6,'Android':7,'Chrome OS':8}
train_data.OpSys = [OpSys[item] for item in train_data.OpSys]
file1=r'C:\Users\KIIT\Documents\AndroidStudio\DeviceExplorer\Pixel_API_27 [emulator-5554]\data\data\com.example.myapplicationnew\files\text1.txt'
f = open(file1,"r")
str=f.read()
newarr=[]
print(str)
for i in str:
    if(i != ',')&(i!='\n'):
           newarr.append(i)
n1=len(newarr)
print(n1)
print(newarr)
a1=10*float(newarr[0])+float(newarr[1])
a2=10*float(newarr[2])+float(newarr[3])
print(a2)
a3=float(newarr[4])
a4=float(newarr[5])
if(n1==9):
    a5=(100*float(newarr[6])+10*float(newarr[7])+float(newarr[8]))
else:
    a5 = (1000*float(newarr[6]) + 100*float(newarr[7]) + 10*float(newarr[8])+float(newarr[9]))
t=[a1,a2,a3,a4,a5]
print(t)


f.close()
X=train_data.ix[:,(1,4,7,11,12)].values
neigh=NearestNeighbors(n_neighbors=20).fit(X)
res=neigh.kneighbors([t],return_distance=False)
p=[]
b=[]
c=[]

for i in range(20):
    r = res[0][i]
    temp=train_data['Company'][r]


    if(temp==1):
       p.append(train_data['Product'][r])
       b.append(train_data['rating'][r])
       c.append(train_data['TypeName'][r])

d=list(zip(p,b,c))
print("-----------------THE RECCOMENDED PRODUCTS------------------")
print(" ")
for i in d:
    print(i)
numrows = len(d)

srt=sorted(d,reverse=True, key=lambda x: (x[1]))
print("The final  five reccomended products are:")
print("-----------------THE RECCOMENDED PRODUCTS ON BASIS OF RATING------------------")
res=[]
for i in range(numrows):
    print(srt[i][0])
    res.append(srt[i][0])
print(res)
review=[]
for i in train_data['rating']:
    if(i==1):
        review.append("worst")
    if (i==2):
        review.append("bad")
    if (i==3):
        review.append("average")
    if (i==4):
        review.append("good")
    if(i==5):
        review.append("best")

train_data['review']=review
#print(train_data)

#export_csv=train_data.to_csv(r'C:\Users\KIIT\PycharmProjects\MachineLearningProject\dellproject\train_data.cvs',index=None,header=True)

#print(train_data['TypeName'])


def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)

List=c

file=r'C:\Users\KIIT\AndroidStudioProjects\Dell\app\src\main\res\raw\text4.txt'
with open(file, 'w') as f:
    for item in res:
        f.write("%s\n" % item)

f.close()
if(most_frequent(List)==2):
    print("---------------YOU CAN  ALSO BUY ----------------")
    print(" ")

    print("1.JOYSTICKS")
    print("2.GRAPHICS CARD")
    print("3.HEADPHONES")
    print("MEMORY CARD")
    p1=['JOYSTICKS','GRAPHICS CARD','HEADPHONES','HEADPHONES','MEMORY CARD']
    file1=r'C:\Users\KIIT\AndroidStudioProjects\Dell\app\src\main\res\raw\textfile.txt'
    with open(file1, 'w') as f1:
        for item in p1:
            f1.write("%s\n" % item)
else:
    print("---------------YOU CAN  ALSO BUY ----------------")
    print(" ")
    print("The reccomended products are:")
    print("1.EXTERNAL HARDDRIVE")
    print("2.EARPHONES")
    print("3.MEMORY CARD")
    print("4.WIRELESS MOUSE")
    print("5.Wireless KEYBOARD")
    c1=['EXTERNAL HARDDRIVE','EARPHONES','MEMORY CARD','WIRELESS MOUSE','Wireless KEYBOARD']
    file1 = r'C:\Users\KIIT\AndroidStudioProjects\Dell\app\src\main\res\raw\textfile.txt'
    with open(file1, 'w') as f1:
        for item in c1:
            f1.write("%s\n" % item)
f1.close()
#count=0
#for i, g in train_data.groupby(['Company','rating']):
 #   print(g)
hnames = ['Company','TypeName','Inches','Ram','OpSys','Price_euros','rating']




correlations = train_data.corr()

print( correlations  )

#plotcorrelation matrix
fig = plt.figure()
#Following will add matrix and side bar in entire area
subFig = fig.add_subplot(111)

cax = subFig.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)

#-----------------------------
ticks = np.arange(0,8,1)   # It will generate values from 0....8
subFig.set_xticks(ticks)
subFig.set_yticks(ticks)
subFig.set_xticklabels(hnames)
subFig.set_yticklabels(hnames)
#-----------------------------
#train_data.plot(kind='density', subplots=True,
 #                 layout=(3,3), sharex=False)
#scatter_matrix(train_data)
plt.show()
#train_data.hist()
averagecost=train_data.groupby('Company', as_index=False)['Price_euros'].mean()
print(averagecost)
plt.figure(2)
plt.plot(np.array(averagecost['Company']),np.array(averagecost['Price_euros']),'go-',label='line1',linewidth=2)
plt.xlim(1,19)
plt.show()











