import model

m = model.Model()

print("\nDefault Model : {}".format(m))

print("\n######TEST FONCTION IK######")

print("\nsetting a speed to motor 1 only")
m.m1.speed = 0.1
linear_speed, rotational_speed = m.dk()
print("\nlinear_speed = {}\nrotational_speed = {}".format(linear_speed, rotational_speed))

print("\nsetting a speed to motor 1 and 2")
m.m1.speed = 0.1
m.m2.speed = 0.1
linear_speed, rotational_speed = m.dk()
print("\nlinear_speed = {}\nrotational_speed = {}".format(linear_speed, rotational_speed))

print("\nparametre moteur 1 negatif et moteur 2 positif")
m.m1.speed = -0.1
m.m2.speed = 0.1
linear_speed, rotational_speed = m.dk()
print("\nlinear_speed = {}\nrotational_speed = {}".format(linear_speed, rotational_speed))

print("\nparametre moteur 1 positif moteur 2 negatif")
m.m1.speed = 0.1
m.m2.speed = -0.1
linear_speed, rotational_speed = m.dk()
print("\nlinear_speed = {}\nrotational_speed = {}".format(linear_speed, rotational_speed))

print("\n######TEST FONCTION DK######")

print("\nparametre ")
linear_speed = 1
rotational_speed = 0
m.m1.speed, m.m2.speed = m.dk()
print("\nMOTEUR 1 = {}\nMOTEUR 2 = {}".format(m.m2.speed, m.m2.speed))