class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(f"Rectangle sides: {rect.sides}")
    print(f"Square of rectangle: {rect.get_square()}")
