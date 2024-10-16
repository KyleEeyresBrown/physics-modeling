from __future__ import division
from visual import *
wallR = box(pos=(1.75e11,1.2e11,0),size=(4e10,6e11-2e11,4e11),color=color.green)
wallL = box(pos=(-3e11,1.2e11,0),size=(4e10,6e11-2e11,4e11),color=color.green)
wallU = box(pos=(-6.4e10,3e11,0),size=(6e11-.8e11,4e10,4e11),color=color.green)
wallB = box(pos=(-6.4e10,-.7e11,0),size=(6e11-.8e11,4e10,4e11),color=color.green)
Sun = sphere(pos=vector(0,0,0), radius=3e10, color=color.yellow)#, make_trail=True,retain=2300)
Earth = sphere(pos=vector(1.5e11,0,0), radius=5e9, color=color.green)#, make_trail=True,retain=2300)
Jupiter = sphere(pos=vector(1e11,2.5e11,0), radius=10e9, color=color.orange)#,make_trail=True,retain=2300)
Moon = sphere(pos=vector(1.25e11,0,0), radius=2.5e9, color=color.white)#,make_trail=True,retain=500)
Mars = sphere(pos=vector(-1e11,0,0), radius=3e9, color=color.red)#,make_trail=True,retain=1000)
scene.autoscale = 0
G=6.67e-11

Sun.m = 1.989e30
#Earth.m = 1e30
Earth.m = 5.972e24
Moon.m=7.35e22
Mars.m=6.39e23
Jupiter.m=1.898e27

Sun.p = vector(0,0,0)
#Earth.p=vector(0,3e34,0)
#Earth.p=vector(0,1.77e29,0)
Earth.p=vector(0,1.65e29,0)
Mars.p=vector(0,3e28,0)
Jupiter.p=vector(-2e31,3e30,0)
Moon.p=vector(0,1.77e26,0)

deltat = 1e4
t=0

Fscale=1.75e9/1e21
pscale =2e10/1e29
#parr = arrow(color=color.red)
#parrF = arrow(color=color.blue)

while 1==1:

    rate(300)

    r=Earth.pos-Sun.pos
    r2=Moon.pos-Earth.pos
    r3=Mars.pos-Sun.pos
    r4=Jupiter.pos-Sun.pos

    F=-(r*G*Sun.m*Earth.m)/mag(r)**3
    F2=-(r2*G*Moon.m*Sun.m)/mag(r2)**3
    F3=-(r3*G*Sun.m*Mars.m)/mag(r3)**3
    F4=-(r4*G*Sun.m*Jupiter.m)/mag(r4)**3

    Earth.p = Earth.p+F*deltat
    #Sun.p = F*deltat
    Moon.p = Moon.p+F2*deltat
    Mars.p = Mars.p+F3*deltat
    Jupiter.p = Jupiter.p+F4*deltat

    Earth.pos = Earth.pos+Earth.p*deltat/Earth.m
    #Sun.pos = Sun.pos+Sun.p*deltat/Sun.m
    Moon.pos = Moon.pos+Moon.p*deltat/Moon.m
    Mars.pos = Mars.pos+Mars.p*deltat/Mars.m
    Jupiter.pos = Jupiter.pos+Jupiter.p*deltat/Jupiter.m

    if Earth.x + 5e9 +2e10 > wallR.x:
        Earth.p.x = -Earth.p.x
    if Earth.x -5e9 -2e10 < wallL.x:
        Earth.p.x = -Earth.p.x
    if Earth.y  + 5e9 +2e10 > wallU.y:
        Earth.p.y = -Earth.p.y
    if Earth.y -5e9 -2e10 < wallB.y:
        Earth.p.y = -Earth.p.y
        
    if Mars.x + 3e9 +2e10 > wallR.x:
        Mars.p.x = -Mars.p.x
    if Mars.x -3e9 -2e10 < wallL.x:
        Mars.p.x = -Mars.p.x
    if Mars.y + 3e9 +2e10 > wallU.y:
        Mars.p.y = -Mars.p.y
    if Mars.y - 3e9 -2e10 < wallB.y:
        Mars.p.y = -Mars.p.y

    if Moon.x + 3e9 +2.5e9 > wallR.x:
        Moon.p.x = -Moon.p.x
    if Moon.x -3e9 -2.5e9 < wallL.x:
        Moon.p.x = -Moon.p.x
    if Moon.y + 3e9 +2.5e9 > wallU.y:
        Moon.p.y = -Moon.p.y
    if Moon.y - 3e9 -2.5e9 < wallB.y:
        Moon.p.y = -Moon.p.y
        
    if Jupiter.x + 10e9 +2e10 > wallR.x:
        Jupiter.p.x = -Jupiter.p.x
    if Jupiter.x -10e9 -2e10 < wallL.x:
        Jupiter.p.x = -Jupiter.p.x
    if Jupiter.y  + 10e9 +2e10 > wallU.y:
        Jupiter.p.y = -Jupiter.p.y
    if Jupiter.y -10e9 -2e10 < wallB.y:
        Jupiter.p.y = -Jupiter.p.y

    #parr.pos= Earth.pos+Earth.p*deltat/Earth.m
    #parr.axis= Earth.p*pscale
    #parrF.pos= Earth.pos+Earth.p*deltat/Earth.m
    #parrF.axis= F*Fscale
    
    t=t+deltat

    #print "F=", F
    
    
