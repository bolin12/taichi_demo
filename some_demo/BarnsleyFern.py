import taichi as ti
import math

ti.init(arch=ti.gpu)

width = 660
height = 1000
pixels = ti.Vector(3, dt=ti.f32, shape=(width, height))


@ti.func
def generatePoint(x, y, t):
    r = ti.random()
    nextX = 0.0
    nextY = 0.0

    if(r < 0.01):
        nextX = 0
        nextY = 0.16*y
    elif(r < 0.85):
        nextX = 0.85*x + (0.04+t)*y
        nextY = -(0.04+t)*x + 0.85*y + 1.6
    elif(r < 0.93):
        nextX =  0.20*x + -0.26*y
        nextY = 0.23*x + 0.22*y + 1.0
    else:
        nextX =  -0.15*x + 0.28*y
        nextY = 0.26*x + 0.24*y + 0.44
    return nextX, nextY

@ti.kernel
def drawPoint(t: ti.f32):
    for i in range(0, 100000):
        x = 0.0
        y = 0.0
        for j in range(0, 40):
            x, y = generatePoint(x, y, t)
            pixels[(int)((x/6+0.5)*width), (int)(y*height/10.5)][0] += 0.01
            pixels[(int)((x/6+0.5)*width), (int)(y*height/10.5)][1] += 0.02
            pixels[(int)((x/6+0.5)*width), (int)(y*height/10.5)][2] += 0.005
gui = ti.GUI("BarnsleyFern", (width, height))
timer = 0.0
while(True):
    timer += 0.08
    drawPoint(math.sin(timer)*0.03)#固定时间周期
    gui.set_image(pixels)
    gui.show()
    pixels.fill(0)

