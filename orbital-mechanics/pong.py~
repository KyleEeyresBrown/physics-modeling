from visual import *
ball = sphere(pos=(-5,0,0), radius=1, color=color.yellow)
wallR = box(pos=(6,0,0),size=(0.2,40,12),color=color.green)
wallL = box(pos=(-6,0,0),size=(0.2,40,12),color=color.green)
wallU = box(pos=(0,6,0),size=(6,0.2,12),color=color.green)
wallB = box(pos=(0,-6,0),size=(6,0.2,12),color=color.green)
wallUU = box(pos=(0,20,0),size=(12,0.2,12),color=color.green)
wallBB = box(pos=(0,-20,0),size=(12,0.2,12),color=color.green)
ball.velocity = vector(2,1.5,0)
wallB.velocity = vector(3,0,0)
wallU.velocity = vector(-3,0,0)
dt = 0.05
while (1==1):
    rate(100)
    ball.pos = ball.pos + ball.velocity*dt
    wallB.pos = wallB.pos + wallB.velocity*dt
    wallU.pos = wallU.pos + wallU.velocity*dt
    if ball.x + 1 > wallR.x:
        ball.velocity.x = -ball.velocity.x
    if ball.x -1 < wallL.x:
        ball.velocity.x = -ball.velocity.x
    if ball.y + 1 > wallU.y and ball.x > wallU.pos.x -4 and ball.x > wallU.pos.x +4:
        ball.velocity.y = -ball.velocity.y
    if ball.y - 1 < wallB.y and ball.x > wallB.pos.x -4 and ball.x > wallB.pos.x +4:
        ball.velocity.y = -ball.velocity.y
    if ball.y + 1 > wallUU.y:
        ball.velocity.y = -ball.velocity.y
    if ball.y - 1 < wallBB.y:
        ball.velocity.y = -ball.velocity.y
    if wallB.x +3 > wallR.x:
        wallB.velocity.x = -wallB.velocity.x
    if wallB.x -3 < wallL.x:
        wallB.velocity.x = -wallB.velocity.x
    if wallU.x +3 > wallR.x:
        wallU.velocity.x = -wallU.velocity.x
    if wallU.x -3 < wallL.x:
        wallU.velocity.x = -wallU.velocity.x


