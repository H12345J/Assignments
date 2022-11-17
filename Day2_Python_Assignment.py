#!/usr/bin/env python
# coding: utf-8

# In[ ]:


continuation with Strings:


# In[2]:


full_name='Ravi Chandra'
print(full_name)


# In[3]:


print(full_name.title())


# In[4]:


#I want to get name in full letters
print(full_name.upper())


# In[6]:


#I want to get complete full name in small case
full_name='Neeta Geetha'
print(full_name.lower())


# In[ ]:


introduction to f strings
#general Syntax of f strings


# In[9]:


print(f" customer words {placeholder -1}{placeholder -2}........{placeholder......n}")


# In[14]:


first_name='varun'
last_name='kumar'
#I want to get the full name....?
print(f"{first_name} {last_name}")


# In[16]:


full_name=f"{first_name} {last_name}"
print(full_name)


# In[17]:


print(full_name.title())


# In[18]:


# req: to appreciate varun
print(f"keep up the good work,{full_name.title()}")


# In[ ]:


Adding whitespaces to strings:


# In[19]:


print("favourite_languages:pythonjavac++cobolpascal")


# In[20]:


print("favorite_languages:\npython\njava\nc++\ncobol\npascal") # \n ------> is a new line delimiter


# In[21]:


print("favorite_languages:\n\tpython\n\tjava\n\tc++\n\tcobol\n\tpascal")# \t-----> is a tab delimiter


# In[ ]:


Removing whitespaces from strings


# In[22]:


name='python'
print(name)


# In[23]:


name2='   python'
print(name2)


# In[24]:


print(name2.lstrip()) # left strip=====> only targets on the left


# In[26]:


name3='python   '
print(name3.rstrip())  #right strip====> only targets on the right


# In[27]:


name4='   python   '
print(name4.strip())   #search operation


# In[ ]:




