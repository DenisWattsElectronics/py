import math

D = 5
N = 3
M = 10000



v_cube = D**3
v_cube_small = (D/M)**3
v_sphere_small = (4/3)*((D/(2*M))**3)*math.pi

print("v_cube_small =", v_cube_small)
print("v_sphere_small =", v_sphere_small)

v_cube_complete_M = v_cube_small*M**3
v_sphere_complete_M = v_sphere_small*M**3

print("v_cubcomplete =", v_cube_complete_M)
print("v_sphere_complete =", v_sphere_complete_M)







