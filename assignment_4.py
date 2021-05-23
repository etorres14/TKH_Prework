#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 4
def longest(names):
    longest_name = ''
    for name in names:
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name

big_name = longest(names_list)
print (big_name)

