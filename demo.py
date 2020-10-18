import taichi as ti
import random
ti.init(arch=ti.gpu)
total_num_particle = 25

x = ti.Vector(2,dt=ti.f32, shape=total_num_particle)
v = ti.Vector(2,dt=ti.f32, shape=total_num_particle)

f = ti.Matrix(2,2, dt=ti.f32, shape=(total_num_particle, total_num_particle))

A = ti.Matrix(2,2, dt=ti.f32, shape=(total_num_particle, total_num_particle))
b = ti.Vector(2,dt=ti.f32, shape=total_num_particle)

J = ti.Matrix(2,2, dt=ti.f32, shape=(total_num_particle, total_num_particle))

dt = 1e-3
m_1 = 1

I = ti.Matrix([
            [1.0, 0.0],
            [0.0, 1.0]
        ])
a = ti.Vector([1.0,2.0])
# b = ti.Vector(1,ti.f32, shape=(2))
# C = ti.Vector(1, dt=ti.f32, shape=2)

@ti.kernel
def demo():

    b = a.outer_product(a)
    print(b,b.n)
    print(a.n)
    print(a)
    for i in ti.static(range(2)):
        for j in ti.static(range(2)):
            print(i,j, "-th component is", b[i,j])

demo()


