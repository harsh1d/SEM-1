import math


class Circle:

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * (self.radius**2)


# Create a Circle object with a radius of 5
circle = Circle(5)

# Display the area of the circle
print(f"The area of the circle is: {circle.area()}")