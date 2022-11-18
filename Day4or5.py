#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Continuation with list


# In[ ]:


organising the list datatype:


# In[1]:


cars = ['kia','hyundai','audi','suzuki','bmw','maruti','benz']
print(cars)

#req : I want to arrange the above car brands in the alphabetical order.....A to Z order
# In[ ]:


2 approaches:
    1.Temporary approach------> we can have the origional order of the list declared=====>sorted
    2.Permanent approach------> the changes will be applied permanently=======>sort


# In[2]:


print(cars.sort())


# In[3]:


print(sorted(cars))


# In[ ]:


benz and bmw =====> b,b e and m


# In[4]:


print(cars)


# In[5]:


cars.sort()


# In[ ]:


get_ipython().set_next_input('Interview question: what is a difference between sort and sorted methods in a list');get_ipython().run_line_magic('pinfo', 'list')


# In[ ]:


I want to print the entire list in the reverse order ----> Z to A


# In[6]:


cars.reverse()


# In[7]:


print(cars)


# In[8]:


#I want to count the no of elements in the list
print(len(cars))


# In[ ]:


Introduction to slicing:
    [startvalue:stopvalue:stepcount]
    Note: always stop value is exclusive,to include the stop value we have to increment the index number +1.


# In[9]:


students = ['shashank','ariba','naveena','ramesh','kiran','vasu','hameed']
type(students)


# In[10]:


print(students)


# In[11]:


#I want to include shashank and areeba
print(students[0:2])


# In[12]:


print(students[2:4])


# In[ ]:




