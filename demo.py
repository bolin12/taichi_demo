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
@ti.kernel
def demo():
    # for i in range(int(total_num_particle)):
    #     for j in range(int(total_num_particle)):
        
    #         J[i,j]=I
    for i in range(int(total_num_particle)):
        for j in range(int(total_num_particle)):
            print(J[i,j])

demo()

