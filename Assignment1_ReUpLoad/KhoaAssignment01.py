
# coding: utf-8

# In[2]:

import csv
import numpy as np
import operator as op
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

Savename =[]
i=0
k=0
m=0
IndexName=[]
LabelName=[]
LabelValue=[]

with open ('datagovdatasetsviewmetrics.csv','rb') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    header = readCSV.next() #discard the first row from the file
    for row in readCSV:
        i+=1
        Savename.append(row)
    s1= "The number of total records is : "
    s2= "------***-----***---------"
    print ("{0:^50} {1}".format(s1,i))
    print ("{:^60}".format(s2))
    
          
    topviews = [(row [2],int(row[3])) for row in Savename]
    topviews.sort(key=lambda x:x[1]) #sort views
    topviews.reverse() #Reverse the order, max to min
    topviews = topviews[:10]   #Take the top ten max value
    print("{0:-<55}  {1}".format("Top Ten organizations","Total views"))
    for row in topviews:
        print ("{0:-<55}  {1}".format(row[0],str(row[1])))
    
    #Configure values to draw graph
    for row in topviews:
        m+=1
        IndexName.append(m)
        LabelName.append(row[0])
        LabelValue.append(row[1])
        

    #Begin of graph 
    plt.yticks(IndexName,LabelName)
    plt.barh(width=LabelValue,bottom=IndexName,align='center')
    
    
    plt.title('Assigment 1')
    plt.ylabel('Name of Organiztion')
    plt.xlabel('Total views')
    plt.show()

