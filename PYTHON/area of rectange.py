class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Create three different Rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(6, 3)
rectangle3 = Rectangle(8, 4)

# Function to display the area of a rectangle
def display_area(rectangle):
    print(f"The area of the rectangle is: {rectangle.area()}")

# Display the area of all three rectangles
display_area(rectangle1)
display_area(rectangle2)
display_area(rectangle3)