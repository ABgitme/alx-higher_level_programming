from models.base import Base


class Rectangle(Base):
    """
    Class that represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y coordinate of the rectangle. Defaults to 0.
            id (int, optional): The unique identifier of the object. Defaults to None.
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x coordinate of the rectangle."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y coordinate of the rectangle."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the rectangle with the "#" character."""
        for y in range(self.y):
            print()  # Add empty lines for y-axis offset

        for _ in range(self.height):
            for x in range(self.x):
                print(" ", end="")  # Add spaces for x-axis offset
            print("#" * self.width)

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return (self.width + self.height) * 2

    def __str__(self):
        """String representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        """ Updates the attributes of the rectangle."""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            try:
                self.width = args[1]
            except (TypeError, ValueError):
                pass
        if len(args) >= 3:
            try:
                self.height = args[2]
            except (TypeError, ValueError):
                pass
        if len(args) >= 4:
            try:
                self.x = args[3]
            except (TypeError, ValueError):
                pass
        if len(args) >= 5:
            try:
                self.y = args[4]
            except (TypeError, ValueError):
                pass