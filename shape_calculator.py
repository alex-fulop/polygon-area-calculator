class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={0}, height={1})".format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            shape = ''
            for i in range(self.height):
                shape = shape + "*" * self.width + '\n'
            return shape

    def get_amount_inside(self, shape):
        width_diff = self.width / shape.width
        height_diff = self.height / shape.height
        return int(width_diff * height_diff)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return "Square(side={0})".format(self.height)

    def set_side(self, side):
        self.set_width(side)

    def set_width(self, side):
        self.set_height(side)

    def set_height(self, side):
        self.height = side
        self.width = side
