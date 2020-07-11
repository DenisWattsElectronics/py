
n_slices = 100
slices_coord = [0.0]*n_slices
slices = [0]*n_slices
sq_slices = [0]*(n_slices-1) 
sq = 0
a = 2
b = 4
slices_delta = 0.0

def integrand(x):
    y = x
    return y    

def antiderivative(x):
    y = (x**2)/2
    return y

#-------
def Newton_Leibniz(a, b):
    nl = antiderivative(b) - antiderivative(a)
    return nl
NL = Newton_Leibniz(0, n_slices)
#-------

slices_delta = (b-a)/n_slices
slices_coord[0] = a
for i in range (1, n_slices):
    slices_coord[i] = slices_coord[i-1] + slices_delta

for i in range(0, n_slices):
    slices[i] =  integrand(slices_coord[i])

for i in range(0, n_slices-1):
    sq_slices[i] = (slices[i+1] - slices[i])*slices[i]
    
for i in range(0, n_slices-2):
    sq = sq + sq_slices[i]












# print("slices =",slices)
# print("")
# print("")
print("sq =",sq)
# print("")
print("NL =",NL)

# print("slices_coord =",slices_delta)
# print("")
# print("slices_coord =",slices_coord)
# print("")
# print("slices =",slices)



