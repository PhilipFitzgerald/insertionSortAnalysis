#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd


# In[3]:


counter = 0


# In[4]:


def addToList(listValues, size):
    for i in range(size):
        listValues.append(random.randint(1,100))


# In[5]:


def insertionSort(arr): 
    counter = 0
    for i in range(1, len(arr)): 
        key = arr[i] 
        counter+=1;
        j = i-1
        counter+=1;
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j]
                counter+=1;
                j -= 1
        arr[j+1] = key
        counter+=1;
    return counter


# In[6]:


listValues=[]
listcount=[]
temp=[]
x =[]
y=[]
expected=[]
listTable=[]
listSizes = [10,20,30,40,50,60,70,80,90,100]
sizeCounter=0
sets = 10
i =1
while sets > 0:
    size = listSizes[sizeCounter]
    addToList(listValues, listSizes[sizeCounter])
    print(str(i) + " Unsorted data is: ", listValues)
    counts = insertionSort(listValues)
    x.append(size)
    y.append(counts)
    expected.append(size**2)
    temp.append(size)
    temp.append(counts)
    temp.append(size**2)
    listTable.append(temp[:])
    temp.clear();
    print("  Sorted data is:   ", listValues, "\n")
    listValues.clear()
    sizeCounter+=1;
    i+=1;
    sets-=1;


# In[7]:


plt.plot(x,y)
plt.plot(x,expected)
plt.xlabel("Input data #s")
plt.ylabel("Steps count")
plt.show()


# In[8]:



df = pd.DataFrame(listTable, columns=['N', 'Steps', 'Worst Case'])
print(df)

