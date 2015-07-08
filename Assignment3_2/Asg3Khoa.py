#test assignment 3
#https://rstudio-pubs-static.s3.amazonaws.com/44557_aec58e755ad7429cac8ba9bff382d930.html
import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime


Maxstep1 =[]
steps =[]
dates =[]
i=0
j=0
k=0
N=0
indexdate =[]
y_value =[]
afile='activity.csv'
try:
      f=open(afile)
      data1=f.read()
      f.close()
except IOError:
      print ("Cannot find file: " + afile)
      exit()

with open(afile,'rb') as csvfile:
      readCSV = csv.reader(csvfile, delimiter =',')
      header = readCSV.next()
      for item in readCSV:
            k+=1        #The total record of data
            if item[0] =='NA':
                  i+=1  #Keep track of the data that is Not Applicable
            if item[0] =='0':
                  j+=1  #Keep track of the number without activity
            if item[0] !='NA':
                  steps.append(item)

      Maxstep1 = [(int(item[0]),item[1]) for item in steps]
      Maxstep1.sort(key=lambda x:x[0])
      Maxstep1.reverse()
      Maxstep2= Maxstep1[:20] #use these 20 values to draw a chart
      Maxstep1 = Maxstep2[:10] #use these ten max values to print out

      print "Total record is " +str(k)+"\n"
      print "The number of data that is Not Applicable is " + str(i)+"\n"
      print "The number of the day without activity is " + str(j)+"\n"
      print "\n"
      print "The top 10 max number of steps"
      print ("{0:<55} {1}".format("The number of steps","The date"))
      for x in Maxstep1:
            print ("{0:-<55} {1}".format(str(x[0]),str(x[1]))) +"\n"
            
      print "\n"
      print "The chart of the activity" + "\n"
      
      #Begin to the chart
      
      Maxstep2.sort(key= lambda x:x[1])
      
      for row in Maxstep2:
            da=row[1]
            y_value.append(row[0])
            dates.append(datetime.datetime.strptime(da,"%Y-%m-%d").date())
      
      print "---------------------------------------------"       

      plt.plot(dates,y_value,':rs')
      plt.gcf().autofmt_xdate()
      plt.title ('Assignment 3')
      plt.ylabel('The steps - activity')
      plt.xlabel('The date')
      plt.show()
      
      
                 
            
            
            
            
            

