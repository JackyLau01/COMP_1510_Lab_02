size_of_can = 4

coverage = 400

length = float(input('please enter a length'))

width = float(input('please enter a width'))

height = float(input('please enter a height'))

coats = float(input('please enter a number of coats'))

surface_area = 2 * length * height + 2 * width * height + length * width

coverage_needed = surface_area * coats

cans_of_paint_required = coverage_needed / coverage

print(str('you will need'), float(cans_of_paint_required), str('cans of paint.'))
