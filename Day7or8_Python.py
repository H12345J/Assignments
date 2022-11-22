#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to Dictionary Datatype:


# In[ ]:


Definition: A dictionary is a combination of key value pairs.
    Classificaton: It is classified as a mutable datatype
        How to define the dictionary.....?========>{}


# In[ ]:


# req: alien ====>


# In[1]:


alien = {'color':'green','points':5}
print(alien)


# In[2]:


type(alien)


# In[ ]:


# req: how to access the key value pairs.
#give the key and get the value.
#I want to know the color  of the alien...?


# In[3]:


print(alien['color'])


# In[5]:


print(alien['points'])


# In[ ]:


# req: how to add new key value pairs to the dictionary.....?
# req : start position-----> 0


# In[7]:


alien['start_position']=0
print(alien)


# In[ ]:


can I give the value and get the key.....? =====> No. It is not accepted, only we can give the key and get the value


# In[10]:


print(alien['points'])
print(alien)


# In[13]:


alien['points']=110
print(alien)


# In[ ]:


# req: How to delete the key  value pairs.....?


# In[15]:


del alien['points']
print(alien)


# In[ ]:


# create a user account in facebook.....?


# In[17]:


user_account={'user_name':'codetrainingacademy','firstname':'code','lastname':'training','dob':'01-01-2021','password':'12345'}
print(user_account)


# In[18]:


print(user_account['firstname'])


# In[ ]:


# implementation of a for loop on the dictionary
key, value


# In[ ]:


# general syntax  of a for loop.
for tempvar1, tempvar2 in mainvar.items():
    print(tempvar1)
    print(tempvar2)


# In[21]:


for x,y in user_account.items():
    print(x)
    print(y)


# In[28]:


for x,y in user_account.items():
    print(f"key:{x}")
    print(f"value:{y}.\n")


# In[ ]:


I want to get only the keys....?


# In[31]:


for a in user_account.keys():
    print(f"key:{a}")


# In[ ]:


I want to get  only the values....?


# In[32]:


for b in user_account.values():
    print(f"values:{b}")


# In[ ]:


Thank you.

