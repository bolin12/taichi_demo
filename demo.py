import taichi as ti
import random
ti.init(arch=ti.gpu)
total_num_particle = 25

x = ti.Vector(2,dt=ti.f32, shape=total_num_particle)
v = ti.Vector(2,dt=ti.f32, shape=total_num_particle)

f = ti.Matrix(2,2, dt=ti.f32, shape=(total_num_particle, total_num_particle))

A = ti.Matrix(2,2, dt=ti.f32, shape=(total_num_particle, total_num_particle))
b = ti.Vector(2,dt=ti.f32, shape=total_num_particle)

dt = 1e-3
m_1 = 1

