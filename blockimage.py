#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as nmp
frame = nmp.zeros([600,600,3], nmp.uint8)

def link_points(point1,point2):
    return cv2.line(frame,point1,point2,color,3)

color = (255,0,255)
p1 = (100,100)
p2 = (100,200)
p3 = (200,200)
p4 = (200,100)
p5 = (150,50)
p6 = (150,150)
p7 = (250,150)
p8 = (250,50) 
dI = link_points(p1,p2)
dI = link_points(p2,p3)
dI = link_points(p3,p4)
dI = link_points(p1,p4)
dI = link_points(p5,p6)
dI = link_points(p6,p7)
dI = link_points(p7,p8)
dI = link_points(p5,p8)
dI = link_points(p1,p5)
dI = link_points(p2,p6)
dI = link_points(p3,p7)
dI = link_points(p4,p8)

color = (0,255,0)
p1 = (350,250)
p2 = (350,350)
p3 = (450,350)
p4 = (450,250)
p5 = (400,200)
p6 = (400,300)
p7 = (500,300)
p8 = (500,200)
dI = link_points(p1,p2)
dI = link_points(p2,p3)
dI = link_points(p3,p4)
dI = link_points(p1,p4)
dI = link_points(p5,p6)
dI = link_points(p6,p7)
dI = link_points(p7,p8)
dI = link_points(p5,p8)
dI = link_points(p1,p5)
dI = link_points(p2,p6)
dI = link_points(p3,p7)
dI = link_points(p4,p8)

color = (255,0,150)
p1 = (100,400)
p2 = (100,500)
p3 = (200,500)
p4 = (200,400)
p5 = (150,350)
p6 = (150,450)
p7 = (250,450)
p8 = (250,350) 
dI = link_points(p1,p2)
dI = link_points(p2,p3)
dI = link_points(p3,p4)
dI = link_points(p1,p4)
dI = link_points(p5,p6)
dI = link_points(p6,p7)
dI = link_points(p7,p8)
dI = link_points(p5,p8)
dI = link_points(p1,p5)
dI = link_points(p2,p6)
dI = link_points(p3,p7)
dI = link_points(p4,p8)

cv2.imshow('image',dI)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




