#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=[]
number=int(input("number of elements"))
for i in range(1,number+1):
    value=int(input("enter the value of %d elements:" %i))
    a.append(value)
print("positive numbers in the list are :")
for j in range(number):
    if(a[j]>0):
        print(a[j],end= '  ')
        


# In[ ]:




