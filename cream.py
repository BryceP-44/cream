from turtle import *
import keyboard
from sys import getsizeof
import numpy as np
#getsizeof(a)

x=0
y=0
vx=0
vy=0
ax=0
ay=0

d=.1
size=300
f=.9
og=0#on ground
cont=1
xr,yr,vxr,vyr,br=[],[],[],[],[]
record=[xr,yr,vxr,vyr,br]


while cont==1:
    button=""
    xp=x #x previous
    yp=y #y previous
    
    ax=0
    ay=0
    ay-=2
    vx+=ax*d
    vy+=ay*d
    y+=vy*d
    x+=vx*d
    vxog=vx
    
    if keyboard.is_pressed('left arrow'): #left move
        if 1==1:
            vx-=1
            button+="l"
    if keyboard.is_pressed('right arrow'): #right move
        if 1==1:
            vx+=1
            button+="r"
    if vx>10:
        vx=10
    if vx<-10:
        vx=-10
    if x>size:
        vx=-f*vx
        x=size
        
    if x<-size:
        vx=-f*vx
        x=-size
    if y>size:
        vy=-f*vy
        y=size
    if y<-size:
        vy=0
        og=1
        y=-size
    if keyboard.is_pressed('up arrow'): #jump
        if 1==1:
            vy+=1
            og=0
            button+="u"
            
    if keyboard.is_pressed('down arrow'): #down
        vy-=.5
        button+="d"

    if keyboard.is_pressed('p'): #down
        cont=0
        #bye()
        #done()

    goto(x,y)

    xr.append(x)
    yr.append(y)
    vxr.append(vx)
    vyr.append(vy)
    br.append(button)

import matplotlib.pyplot as plt

print("data loading")

x=xr
y=yr
vx=vxr
vy=vyr


fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(x,y)

xnew=x
ynew=y
vxnew=vx
vynew=vy

def nzmin(vector):
    for i in range(len(vector)):
        if vector[i]>2e-308:
            out=vector[i]
            break
    for i in range(len(vector)):
        if vector[i]<out and vector[i]>2e-308:
            out=vector[i]
    return out

def kd(x,y,vx,vy,a,b):
    dx=x-a
    dy=y-b
    D=np.sqrt(dx**2+dy**2+vx**2+vy**2)
    return D

#minval = np.min(a[np.nonzero(a)])

x=np.array(x,dtype=np.float32)
y=np.array(y,dtype=np.float32)
vx=np.array(vx,dtype=np.float32)
vy=np.array(vy,dtype=np.float32)
trainsteps=100
print("training using",trainsteps,"iterations")
for k in range(trainsteps):
    if k%10==0:
        print("\n",round(k/trainsteps*100),"% total","\n")
    for j in range(len(x)):#go through each point individually
        a,b=x[j],y[j]
        D=kd(x,y,vx,vy,a,b)
        a=np.where(D==np.min(D[np.nonzero(D)]))
        a=int(a[0])
        xnew[j]=(x[j]+x[a])/2
        ynew[j]=(y[j]+y[a])/2
        vxnew[j]=(vx[j]+vx[a])/2
        vynew[j]=(vy[j]+vy[a])/2

print("trained")
ax2.plot(xnew,ynew,"*")

plt.show()


x=xnew
y=ynew
vx=vxnew
vy=vynew


kr=[]
tx=0
ty=0
tvx=0
tvy=0
tax=0
tay=0


seconds=200000
size=700
d=.1
x,y,vx,vy=np.array(x,dtype=np.float32),np.array(y,dtype=np.float32),np.array(vx,dtype=np.float32),np.array(vy,dtype=np.float32)

while True:
    dx,dy,dvx,dvy=x-tx,y-ty,vx-tvx,vy-tvy
    D=np.array(np.sqrt(dx**2+dy**2+dvx**2+dvy**2),dtype=np.float32)
    loc=np.where(D==np.min(D[np.nonzero(D)]))
    loc=int(loc[0])
    a=br[loc]
    """for i in range(len(D)):
        if D[i]==nzmin(D):
            pu()
            #goto(x[i],y[i])
            #goto(tx,ty)
            pd()
            a=br[i]"""

    tay=0
    tay-=2
    tvx+=tax*d
    tvy+=tay*d
    ty+=tvy*d
    tx+=tvx*d
    print(a)
    if "l" in a: #left move
        tvx-=1
    if "r" in a: #right move
        tvx+=1
    if tvx>10:
        tvx=10
    if tvx<-10:
        tvx=-10
    if tx>size:
        tvx=-tvx
        tx=size 
    if tx<-size:
        tvx=-tvx
        x=-size
    if ty>size:
        tvy=-tvy
        ty=size
    if ty<-size:
        tvy=-tvy
        ty=-size
    if "u" in a: #jump
        tvy+=1    
    if "d" in a: #down
        tvy-=.5

    goto(tx,ty)
