#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    #REMOVE SPACES STRING
    s = s.replace(' ','')
    
    #Check if the string is eqaul to the reversed version of the string!
    
    return s == s[::-1]


# In[5]:


palindrome('nurses run')


# In[ ]:




