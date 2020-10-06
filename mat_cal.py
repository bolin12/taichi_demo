import taichi as ti

a = ti.Vector(2,dt=ti.f32, shape=4)
@ti.kernel
def debug():
    for i in range(a.shape[0]):
        a[i] = [1,1]


debug()
print(a*a[None])