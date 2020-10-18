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

A = ti.Matrix([
    [1.0, 2.0],
    [3.0, 4.0]
])
print("A", A)
b = ti.Vector([1.0, 2.0])
print("b", b)
@ti.kernel
def demo():
    c = A @ b
    print(c,c.n)
    d = b.dot(b)
    print(d)
    e = A*A
    print(e)
    f = (A.T() @ A).trace()
    print(f) 

demo()


