#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 5
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
def length_even_odd(names):
    even = []
    odd = []
    even_edit = []
    odd_edit = []
    for name in names:
        if len(name) % 2 == 0:
            even.append(name)
        else:
            odd.append(name)
    for e in even:
        e = "b" + e[1:]
        even_edit.append(e)
    for o in odd:
        o = o[0:(len(o)-1)] + "c"
        odd_edit.append(o)
    print(even_edit)
    print(odd_edit)
    return even_edit
#Sources:
#https://www.w3schools.com/python/python_lists_add.asp
#https://www.programiz.com/python-programming/examples/odd-even

