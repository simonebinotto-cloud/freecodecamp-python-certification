class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return (2*(self.width+self.height))

    def get_diagonal(self):
        return (((self.width**2)+(self.height**2))**0.5)

    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        output = ""
        for i in range(0, self.height):
            for z in range(0, self.width):
                output += "*"
            output += "\n"
        return output

    def get_amount_inside(self, other_shape):
        my_width = getattr(self, 'width', getattr(self, 'side', 0))
        my_height = getattr(self, 'height', getattr(self, 'side', 0))
        other_width = getattr(other_shape, 'width', getattr(other_shape, 'side', 0))
        other_height = getattr(other_shape, 'height', getattr(other_shape, 'side', 0))
        return (self.width // other_width) * (self.height // other_height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_height(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def __str__(self):
        return f"Square(side={self.width})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))