class Rectangle():

  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (self.width*2 + self.height*2)

  def get_diagonal(self):
    return ((self.width**2 + self.height**2) ** 0.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ""
    print (int(self.height))
    for el in range(self.height):
      picture += "*" * self.width
      picture = picture + '\n' if el != self.height else picture
    return picture

  def get_amount_inside(self,sq):
    x = str(sq)
    if 'Square' in x:
      x = x.replace('Square(side=','').replace(")","") 
      side1,side2 = int(x), int(x)
    else:
      x = x.replace('Rectangle(width=','').replace("height=",'').replace(")","").split(",")
      side1 = int(x[0])
      side2 = int(x[1])
    if side1 <= self.width and side2 <= self.height:
      return (self.get_area() // (side1*side2))
    else:
      return 0


class Square(Rectangle):

  def __init__(self,side):
    super().__init__(side,side)

  def set_side(self,side):
    super().set_width(side)
    super().set_height(side)

  def __str__(self):
    return f'Square(side={self.width})'

  def set_width(self, width):
    super().set_width(width)
    super().set_height(width)

  def set_height(self, height):
    super().set_width(height)
    super().set_height(height)