#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Introduction to for loops:
    #general syntax of a for loop:


# In[ ]:


for tempvar in mainvar:
    print tempvar


# In[1]:


students=['anil','varsha','sunil','shekar','ravi','suman']
print(students)


# In[5]:


message=f"How are you?, {students[1].title()}"
print(message)


# In[7]:


message=f"Keep up the good work!{students[4].title()}"
print(message)


# In[16]:


for x in students:
    print(f"Educating people is the best gift to the world. Thank you {x.title()}")


# In[17]:


for x in students:
    print(x)


# In[31]:


for x in students:
    print(f"Wish you all a very happy new year in advance!{x.title()}")
    print(f"Merry Christmas!\n")
print("Give my wishes to your family.Thank you")


# In[ ]:




