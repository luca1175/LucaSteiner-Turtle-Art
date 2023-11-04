#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t
import math as m
import random as rand

## Planet ##
def planet(r):
    t.pencolor('black')
    t.pensize(1)
    t.up()
    t.home()
    t.setpos(0,-r)
    t.down()
    t.fillcolor('orange')
    t.begin_fill()
    t.circle(r)
    t.end_fill()

## Details on Planet##
def details(r,a,d,f):
    t.pencolor((255,99,71))
    t.pensize(5)
    t.up()
    t.home()
    t.left(a)
    t.forward(r-3)
    t.right(a)
    t.down()
    t.circle(r*f, d,1000)

## Stars ##
def stars(n,x,y):
    size = rand.randint(10,20)
    t.up()
    t.setpos(x,y)
    t.down()
    t.fillcolor('yellow')
    t.begin_fill()
    
    if n%2 != 0:
        angle = (180-(180/(n)))
    else:
        angle = (180-(180/(n+1)))
    for i in range(0,n):
        t.forward(size)
        t.right(angle)
    t.forward(size)
    t.end_fill()

## Galaxy

     
def galaxy():
    t.up()
    t.setpos(-350,350)
    t.pensize(0.25)
    t.down()
    for i in range(1,450):
        r = rand.randint(0,255)
        g = rand.randint(0,255)
        b = rand.randint(0,255)
        t.pensize(0.25)
        t.pencolor(r,g,b)
        t.forward(10+i/5)
        t.right(90.911)
      


    

    
## Star Positions ##
def starpos(num):
    ## Q1 ##
    for n in range(0,int(num/2)):
        px1 = rand.randint(0,400)
        py1 = rand.randint(210,400)
        p = rand.randint(5,8)
        stars(p, px1, py1)
    for n in range(0,int(num/2)):
        px1 = rand.randint(210,400)
        py1 = rand.randint(0,400)
        p = rand.randint(5,8)
        stars(p, px1, py1)
    ## Q2 ##               
    for n in range(0,int(num/2)):
        px2 = -1*(rand.randint(210,400))
        py2 = rand.randint(0,400)
        p = rand.randint(5,8)
        stars(p,px2,py2)
    for n in range(0,int(num/2)):
        px2 = -1*(rand.randint(0,400))
        py2 = rand.randint(210,400)
        p = rand.randint(5,8)
        stars(p,px2,py2)
    ## Q3 ##              
    for n in range(0,int(num/2)):
        px3 = -1*(rand.randint(0,400))
        py3 = -1*(rand.randint(210,400))
        p = rand.randint(5,8)
        stars(p,px3,py3)
    for n in range(0,int(num/2)):
        px3 = -1*(rand.randint(210,400))
        py3 = -1*(rand.randint(0,400))
        p = rand.randint(5,8)
        stars(p,px3,py3)
    ## Q4 ##              
    for n in range(0,int(num/2)):
        px4 = rand.randint(210,400)
        py4 = -1*(rand.randint(0,400))
        p = rand.randint(5,8)
        stars(p,px4,py4)
    for n in range(0,int(num/2)):
        px4 = rand.randint(0,400)
        py4 = -1*(rand.randint(210,400))
        p = rand.randint(5,8)
        stars(p,px4,py4)
        
## Rings ##
def rings(theta, Rx, Ry, time, endt):
  
    # red #
    
    t.up()
    xnew = ( Rx * m.cos(time/(2*10*(m.pi)))*m.cos(theta) )- (Ry *m.sin(time/(2*10*(m.pi)))*m.sin(theta) + 0)
    ynew = ( Rx * m.cos(time/(2*10*(m.pi)))*m.sin(theta) )+ (Ry *m.sin(time/(2*10*(m.pi)))*m.cos(theta) + 0)
    t.setpos(xnew,ynew)
    t.down()
    t.pencolor((255, 191, 0))
    t.pensize(40)
   
    for alpha in range(time,endt):
        xnew = ( Rx * m.cos(alpha/(2*10*(m.pi)))*m.cos(theta) )- (Ry *m.sin(alpha/(2*10*(m.pi)))*m.sin(theta) + 0)
        ynew = ( Rx * m.cos(alpha/(2*10*(m.pi)))*m.sin(theta) )+ (Ry *m.sin(alpha/(2*10*(m.pi)))*m.cos(theta) + 0)
        t.setpos(xnew,ynew)
  
    
    ## Orange ##
    if endt > 400:
        time-=10
        endt+=10
    Rx = 1.1*Rx
    Ry = 1.1*Ry
    xnew = ( Rx * m.cos(time/(2*10*(m.pi)))*m.cos(theta) )- (Ry *m.sin(time/(2*10*(m.pi)))*m.sin(theta) + 0)
    ynew = ( Rx * m.cos(time/(2*10*(m.pi)))*m.sin(theta) )+ (Ry *m.sin(time/(2*10*(m.pi)))*m.cos(theta) + 0)
    t.up()
    t.setpos(xnew,ynew)
    t.down()
    t.pencolor((240, 128, 0))
    t.pensize(30)
   
    for alpha in range(time,endt):
        xnew = ( Rx * m.cos(alpha/(2*10*(m.pi)))*m.cos(theta) )- (Ry *m.sin(alpha/(2*10*(m.pi)))*m.sin(theta) + 0)
        ynew = ( Rx * m.cos(alpha/(2*10*(m.pi)))*m.sin(theta) )+ (Ry *m.sin(alpha/(2*10*(m.pi)))*m.cos(theta) + 0)
        t.setpos(xnew,ynew)
    #t.end_fill()
    
    ### Purple ###
    if endt > 400:
        time-=10
        endt+=10
    t.pencolor((255,99,71))
    t.pensize(20)
    Rx = Rx* 1.05
    Ry = Ry *1.04
   
    t.up()
    xnew = ( Rx * m.cos(time/(2*10*(m.pi)))*m.cos(theta) )- (Ry *m.sin(time/(2*10*(m.pi)))*m.sin(theta) + 0)
    ynew = ( Rx * m.cos(time/(2*10*(m.pi)))*m.sin(theta) )+ (Ry *m.sin(time/(2*10*(m.pi)))*m.cos(theta) + 0)
    t.setpos(xnew,ynew)
    t.down()
 
    for alpha in range(time,endt):
        xnew = ( Rx * m.cos(alpha/(2*10*(m.pi)))*m.cos(theta) )- (Ry *m.sin(alpha/(2*10*(m.pi)))*m.sin(theta) + 0)
        ynew = ( Rx * m.cos(alpha/(2*10*(m.pi)))*m.sin(theta) )+ (Ry *m.sin(alpha/(2*10*(m.pi)))*m.cos(theta) + 0)
        t.setpos(xnew,ynew)
 
    
#### Details ####

wn = t.Screen()   
t = t.Turtle()
wn.bgcolor('black')
wn.colormode(255)
t.speed(0)

r = 190
Rx = 250
Ry = 150


###### Drawing Call ########

#starpos(10)
galaxy()

#rings((m.pi/6), Rx, Ry, 0, 198)

planet(r)
details(r,230,31.5,3)
details(r,205,38,3)
details(r,180,38.8,2.8)
details(r,155,40.4,2)
details(r,125,34,1)

#rings((m.pi/6), Rx,Ry, 190,410)


wn.mainloop()


# In[1]:





# In[ ]:





# In[ ]:




