#!/usr/bin/env python
# coding: utf-8

# In[19]:


def bubble_sort(list1):   
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
list1 = [25, 10, 34, 50, 15]  
print("The Elements to be Sorted: ", list1)   
print("The Sorted Elements using Bubble Sort: ", bubble_sort(list1))  


# In[24]:


import pandas as pd

datainput = pd.read_csv("car.csv", delimiter=",")
print(datainput)


# In[ ]:


import pandas as pd
datainput = pd.read_csv("car.csv",delimiter=",")

