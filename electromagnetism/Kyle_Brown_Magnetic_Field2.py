from visual import *

# Variable definitions
pi = 3.14159265259
mu0 = 4*pi*1e-7 # Magnetic permeability
Bscale = 1.2e5
# Scale factor for arrows
R = 0.01
k = 9e9
# Radius of current loop
I = 2.05
# Current in loop
proton = sphere(pos = vector(0.05, 0.01, 0.01), radius = 0.003, color = vector(0, 1, 1), charge = 1.6e-19, m = 1.7e-27, p = vector(-5e-28, -5e-28, 5e-29), trail = curve(color = vector(1, 1, 1)))
electron = sphere(pos = vector(0.05, -0.03, 0.01), radius = 0.003, color = vector(1, 0, 1), charge = -1.6e-19, m = 1.7e-27, p = vector(-5e-28, -5e-28, 5e-29), trail = curve(color = vector(0, 1, 1)))
proton1 = sphere(pos = vector(0.1, -0.03, 0.01), radius = 0.003, color = vector(0, 1, 0), charge = 1.6e-19, m = 1.7e-27, p = vector(-5e-28, -5e-28, 5e-29), trail = curve(color = vector(1, 1, 1)))



loop = ring(pos=vector(0,0,0), axis=vector(1,0,0), radius=R, thickness=0.001)

locations = [ ] # List of locations to calculate the field atz
arrows = [ ] # List of arrows to plot
dtheta = pi/6. # Angle intervals between points
dphi = pi/6.
dRo = .02
# Radius of the sphere of arrows


# Define the set of locations for mapping the magnetic field
for Ro in arange(6*R, 18*R+dRo, dRo):
    for theta in arange(0, pi+dtheta, dtheta):
        x = Ro*cos(theta)
        y = Ro*sin(theta)
        z=0
        a = vector(x, y, z)
        for phi in arange(0, 2*pi, dphi):
            b = rotate(a, angle = phi, axis = vector(1,0,0))
            if b not in locations:
                locations.append(vector(b.x, b.y, b.z))

# Define a set of default arrows for the field
'''for point in locations:
    arrows.append(arrow(pos = point, axis = vector(0.01, 0, 0), color = color.magenta, shaftwidth = 0.002))'''


# Calculating the magnetic field
dalpha = pi/10
#dlarrow = arrow(pos = vector(0,0,0), axis = vector(0,0,0), color = color.red, shaftwidth = 0.005)
#rarrow = arrow(pos = vector(0,0,0), axis = vector(0,0,0), color = color.green, shaftwidth = 0.005)

for Barrow in arrows:
    B = vector(0,0,0)
    for alpha in arange(0, 2*pi, dalpha):
        c = vector(0, R*cos(alpha), R*sin(alpha))
        d = vector(0, R*cos(alpha+dalpha), R*sin(alpha+dalpha))
        dl = d-c
        #dlarrow.pos = c
        #dlarrow.axis = dl
        r = Barrow.pos - c
        #rarrow.pos = dlarrow.pos
        #rarrow.axis = r
        dB=(mu0*I*cross(dl,norm(r)))/(4*pi*mag(r)**2)
        B= B + dB
    Barrow.axis = B*Bscale
    #print mag(Barrow.axis)

# Particle dynamics
dt = .0005
t=0
while t < 1:
    rate(50)
    t = t+dt
    Bproton = vector(0,0,0)
    Bproton1 = vector(0,0,0)
    Belectron = vector(0,0,0)
    for alpha in arange(0, 2*pi, dalpha):
        c = vector(0,R*cos(alpha), R*sin(alpha))
        d = vector(0,R*cos(alpha+dalpha), R*sin(alpha+dalpha))
        dl = d-c
        #dlarrow.pos = c
        #dlarrow.axis = dl
        rproton = proton.pos - c
        rproton1 = proton.pos - c
        relectron = electron.pos - c
        #rarrow.pos = dlarrow.pos
        #rarrow.axis = r
        dBproton=(mu0*I*cross(dl,norm(rproton)))/(4*pi*mag(rproton)**2)
        dBproton1=(mu0*I*cross(dl,norm(rproton1)))/(4*pi*mag(rproton1)**2)
        dBelectron=(mu0*I*cross(dl,norm(relectron)))/(4*pi*mag(relectron)**2)
        Bproton= Bproton + dBproton
        Bproton1= Bproton1 + dBproton1
        Belectron= Belectron + dBelectron
        vproton=proton.p/proton.m
        vproton1=proton1.p/proton1.m
        velectron=electron.p/electron.m
        Fproton1=proton1.charge*cross(vproton1,Bproton1)
        Fproton=proton.charge*cross(vproton,Bproton)
        Felectron=electron.charge*cross(velectron,Belectron)
    r1 = proton.pos - proton1.pos
    r2 = electron.pos - proton1.pos
    r3 = electron.pos - proton.pos
    FE1 = abs(proton.charge*proton1.charge*k)/(mag2(r1))
    FE2 = abs(proton1.charge*electron.charge*k)/(mag2(r2))
    FE3 = abs(proton.charge*electron.charge*k)/(mag2(r3))
    Fonproton1 = FE1*norm(r1) + FE2*norm(r2) + Fproton1
    Fonproton = FE1*norm(r1) + FE3*norm(r3) + Fproton
    Fonelectron = FE2*-norm(r2) + FE3*norm(r3) + Felectron
    proton1.p += Fonproton1*dt
    proton.p += Fonproton*dt
    electron.p += Fonelectron*dt
    proton.pos += (proton.p/proton.m)*dt
    proton1.pos += (proton1.p/proton1.m)*dt
    electron.pos += (electron.p/electron.m)*dt
    t += dt
''' proton.p = proton.p + F*dt
    proton.pos = proton.pos + (proton.p/proton.m)*dt'''



        

