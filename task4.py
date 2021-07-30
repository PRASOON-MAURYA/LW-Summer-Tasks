# IMAGE DRAWING USING CV2

import cv2
import numpy as nmp
frame = nmp.zeros([600,600,3], nmp.uint8)

def draw_cube1(point1,point2):
    return cv2.line(frame,point1,point2,clr1,3)
clr1 = (255,0,255)

p1 = (100,100)
p2 = (100,200)
p3 = (200,200)
p4 = (200,100)
p5 = (150,50)
p6 = (150,150)
p7 = (250,150)
p8 = (250,50)
 
dI = draw_cube1(p1,p2)
dI = draw_cube1(p2,p3)
dI = draw_cube1(p3,p4)
dI = draw_cube1(p1,p4)
dI = draw_cube1(p5,p6)
dI = draw_cube1(p6,p7)
dI = draw_cube1(p7,p8)
dI = draw_cube1(p5,p8)
dI = draw_cube1(p1,p5)
dI = draw_cube1(p2,p6)
dI = draw_cube1(p3,p7)
dI = draw_cube1(p4,p8)



def draw_cube2(point1,point2):
    return cv2.line(frame,point1,point2,clr2,3)
clr2 = (0,255,0)

p1 = (350,250)
p2 = (350,350)
p3 = (450,350)
p4 = (450,250)
p5 = (400,200)
p6 = (400,300)
p7 = (500,300)
p8 = (500,200)

p0 = (100,400)

dI = draw_cube2(p1,p0)
dI = draw_cube2(p1,p2)
dI = draw_cube2(p2,p3)
dI = draw_cube2(p3,p4)
dI = draw_cube2(p1,p4)
dI = draw_cube2(p5,p6)
dI = draw_cube2(p6,p7)
dI = draw_cube2(p7,p8)
dI = draw_cube2(p5,p8)
dI = draw_cube2(p1,p5)
dI = draw_cube2(p2,p6)
dI = draw_cube2(p3,p7)
dI = draw_cube2(p4,p8)


# dI = connect_points(p5,p6)
# dI = connect_points(sq1,sq2)
# dI = cv2.rectangle(frame,rec1,rec2,clr,3)

cv2.imshow('image',dI)
cv2.waitKey()
cv2.destroyAllWindows()
