#!/usr/bin/env python
# coding: utf-8

# In[3]:


import turtle


# In[1]:


t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('#262626')
t.pencolor('#7C909C')
col=('#EDB104','#FFB6C1','#5A2F3D','#B3A3FF')

for n in range(5):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(3)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()


# In[1]:


a='jaina'
a


# In[ ]:




