#!/usr/bin/env python
# coding: utf-8

# In[2]:





import timeit
import random
import matplotlib.pyplot as plt

#Devise an experiment that compares the performance of the del operator on lists and dictionaries.

listYears = [2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]

dicB = {2007 : "Kaka", 2008 : "Cristiano" , 2009 : "Messi", 2010 : "Messi",2011 : "Messi" ,2012 : "Messi",
        2013 : "Cristiano" , 2014 : "Cristiano", 2015 : "Messi" , 2016 : "Cristiano" , 
        2017 : "Cristiano", 2018 : "Modric"}

plotYears = []
plotDic = []

i =0 
j =0 

randNum = 0
del_list_times = []
list_T = []
for i in range(10000, 1000001, 20000):
    list_T = list(range(i))
    randNum = random.randint(0,len(list_T)-1)
    list_time = timeit.timeit('del(list_T[randNum])','from __main__ import list_T, randNum',number = 500)
    #print(list_time)
    #print("the time it took to delete a list is: " + str(list_time))
    plotYears.append(list_time)
        
        
k = 0      
        
def dicC():
    keyS = dicB.keys()
    
    for k in keyS :
        time = timeit.timeit('del dicB[k]' , 'from __main__ import dicB, k', number =0)
    
        #print(k , time *100000)
        plotDic.append(time*100000)




def graph():
    plt.plot(plotYears,  'bs')
    #plt.plot(plotDic, 'ro')
    plt.ylabel('Time taken to get every key')
    plt.xlabel('Iteration')
    #plt.yticks([0.00, 0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00])
    plt.yticks([0.00, 0.5])


#lisTT()
#dicC()
graph()


# In[18]:


import timeit
import random
import matplotlib.pyplot as plt

#Devise an experiment that compares the performance of the del operator on lists and dictionaries.

listYears = [2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]

dicB = {2007 : "Kaka", 2008 : "Cristiano" , 2009 : "Messi", 2010 : "Messi",2011 : "Messi" ,2012 : "Messi",
        2013 : "Cristiano" , 2014 : "Cristiano", 2015 : "Messi" , 2016 : "Cristiano" , 
        2017 : "Cristiano", 2018 : "Modric"}


def dicC():
    keyS = dicB.keys()
    
    for k in keyS :
        time = timeit.timeit('del dicB[k]' , 'from __main__ import dicB, k', number =0)
    
        #print(k , time *100000)
        plotDic.append(time*100000)




def graph():
   # plt.plot(plotYears,  'bs')
    plt.plot(plotDic, 'ro')
    plt.ylabel('Time taken to get every key')
    plt.xlabel('Iteration')
    #plt.yticks([0.00, 0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00])
    plt.yticks([0.00, 0.5])

dicC()
graph()


# In[ ]:




