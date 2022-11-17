#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to List datatypes:
    Definition: A list is a collection of items declared in a particular order.
    Classification: It is classified as a mutable datatype
    How to define or declare list datatype====> []


# In[1]:


Students = ['kumar','Naveed','amala','areeba','keerthi','juveriya'] #0,1,2,3,4,5
print(Students)


# In[ ]:


Understanding the concept of indexing:
    0,1,2,3,4,5..............N


# In[ ]:


#req: I want to access naveed name in output...?


# In[2]:


print(Students[1])


# In[3]:


print(Students[1].title())


# In[ ]:


#How to add/modify/delete elements in the list


# In[5]:


Students.append('Neha')
print(Students)


# In[10]:


Students.insert(4,'Heena')#want  to insert element Heena at index4
print(Students)


# In[11]:


Students.insert(1,'Shashi')#want to insert Shashi at index1
print(Students[1])


# In[13]:


Students[1]='Harish' #want to modify Shashi to Harish
print(Students[1])


# In[14]:


del (Students[0])
print(Students)


# In[ ]:




