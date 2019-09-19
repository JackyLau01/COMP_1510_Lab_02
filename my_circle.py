pi = 3.14159

radius = 0

radius_input = float(input('please enter a radius'))

double_radius = radius_input * 2

circumference = 2 * pi * radius_input

area = pi * radius_input * radius_input

print(circumference)

circumference2 = 2 * pi * double_radius

area2 = pi * double_radius * double_radius

print(str("when the radius is doubled, the circumference is"), float(circumference2 / circumference), str("as long, and the area is"), float(area2 / area), "as large.")

