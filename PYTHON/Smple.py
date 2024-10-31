# import math

# class Shape:
    
#     def __init__(self,radius,side,base,height):
        
#         self.radius=radius
#         self.side=side
#         self.base=base
#         self.height=height
    
#     def area_circle(self, radius):
#         return math.pi * radius ** 2

#     def area_square(self, side):
#         return side ** 2

#     def area_triangle(self, base, height):
#         return 0.5 * base * height
    
# base,height,radius,side = input("ENTER value as base, height,radius,side = ").split()

# base = float(base)
# height = float(height)
# radius = float(radius)
# side = float(side)

# rectangle1 = Shape(radius,side,base,height)

# print(rectangle1.area_circle(radius))
# print(rectangle1.area_square(side))
# print(rectangle1.area_triangle(base, height))
 
 
 # or 
 
import math
class Shape:
    def __init__(self, radius, side, base, height):
        self.radius = radius
        self.side = side
        self.base = base
        self.height = height
    def area(self, shape):
        if shape == 'circle':
            return math.pi * self.radius ** 2
        elif shape == 'square':
            return self.side ** 2
        elif shape == 'triangle':
            return 0.5 * self.base * self.height
        else:
            return None
values = input("Enter values as base, height, radius, side: ").split()
base, height, radius, side = map(float, values)
shape = Shape(radius, side, base, height)
for s in ['circle', 'square', 'triangle']:
    print(f'Area of {s}: {shape.area(s)}')