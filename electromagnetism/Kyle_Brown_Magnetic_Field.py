from visual import *

# Variable definitions
pi = 3.14159265259
mu0 = 4*pi*1e-7 # Magnetic permeability
Bscale = 1.2e5
# Scale factor for arrows
R = 0.01
k = 9e9
# Radius of current loop
I = 1
# Current in loop
proton = sphere(pos = vector(0.02, 0, 0), radius = 0.003, color = vector(0, 1, 1), charge = 1.6e-19, m = 1.7e-27, p = vector(-1e-28, -1e-28, 1e-29), trail = curve(color = vector(1, 1, 1)))
electron = sphere(pos = vector(0, 0, 0), radius = 0.003, color = vector(1, 0, 1), charge = -1.6e-19, m = 1.7e-27, p = vector(-1e-28, -1e-28, 1e-29), trail = curve(color = vector(0, 1, 1)))
proton1 = sphere(pos = vector(-.02, 0, 0), radius = 0.003, color = vector(0, 1, 0), charge = 1.6e-19, m = 1.7e-27, p = vector(-1e-28, -1e-28, 1e-29), trail = curve(color = vector(1, 1, 1)))



loop = ring(pos=vector(-.05,0,0), axis=vector(1,0,0), radius=R, thickness=0.001)
loop2 = ring(pos=vector(.05,0,0), axis=vector(1,0,0), radius=R, thickness=0.001)

locations = [ ] # List of locations to calculate the field at
arrows = [ ] # List of arrows to plot
arrows2 = []
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

#proton.p0 = proton.p
#proton1.p0 = proton1.p
#electron.p0 = electron.p
while t < 2:
    rate(50)
    t = t+dt
    Bproton = vector(0,0,0)
    Bproton1 = vector(0,0,0)
    Belectron = vector(0,0,0)
    B2proton = vector(0,0,0)
    B2proton1 = vector(0,0,0)
    B2electron = vector(0,0,0)
    F = 0
#    proton.p = norm(proton.p)*mag(proton.p0)
#    proton1.p = norm(proton1.p)*mag(proton1.p0)
#    electron.p = norm(electron.p)*mag(electron.p0)
    for alpha in arange(0, 2*pi, dalpha):
        c = vector(-.03,R*cos(alpha), R*sin(alpha))
        d = vector(-.03,R*cos(alpha+dalpha), R*sin(alpha+dalpha))
        dl = d-c
        c2 = vector(.03,R*cos(alpha), R*sin(alpha))
        d2 = vector(.03,R*cos(alpha+dalpha), R*sin(alpha+dalpha))
        dl2 = d2-c2
        #dlarrow.pos = c
        #dlarrow.axis = dl
        rproton = proton.pos - c
        rproton1 = proton.pos - c
        relectron = electron.pos - c
        r2proton = proton.pos - c2
        r2proton1 = proton.pos - c2
        r2electron = electron.pos - c2
        #rarrow.pos = dlarrow.pos
        #rarrow.axis = r
        
        dBproton=(mu0*I*cross(dl,norm(rproton)))/(4*pi*mag(rproton)**2)
        dBproton1=(mu0*I*cross(dl,norm(rproton1)))/(4*pi*mag(rproton1)**2)
        dBelectron=(mu0*I*cross(dl,norm(relectron)))/(4*pi*mag(relectron)**2)
        Bproton= Bproton + dBproton
        Bproton1= Bproton1 + dBproton1
        Belectron= Belectron + dBelectron
        
        dB2proton=(mu0*I*cross(dl2,norm(r2proton)))/(4*pi*mag(r2proton)**2)
        dB2proton1=(mu0*I*cross(dl2,norm(r2proton1)))/(4*pi*mag(r2proton1)**2)
        dB2electron=(mu0*I*cross(dl2,norm(r2electron)))/(4*pi*mag(r2electron)**2)
        B2proton= B2proton + dB2proton
        B2proton1= B2proton1 + dB2proton1
        B2electron= B2electron + dB2electron

        BTproton= B2proton + Bproton
        BTproton1= B2proton1 + Bproton1
        BTelectron= B2electron + Belectron
        
        vproton=proton.p/proton.m
        vproton1=proton1.p/proton1.m
        velectron=electron.p/electron.m
        Fproton1=proton1.charge*cross(vproton1,BTproton1)
        Fproton=proton.charge*cross(vproton,BTproton)
        Felectron=electron.charge*cross(velectron,BTelectron)
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



        

