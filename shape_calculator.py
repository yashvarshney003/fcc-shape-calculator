class Rectangle:
  def __str__(self):
        w = str(self.width)
        h = str(self.height)
        return 'Rectangle(width=' + w + ', height=' + h + ')'


  def __init__(self,width,height = None):
    if(height == None):
      self.width = width
      self.height = width
    else:
      self.width = width
      self.height = height
  def set_width(self,width):
    self.width = width
  def set_height(self,height):
    self.height = height
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2*(self.width +self.height)
  def get_picture(self) :
    if self.width > 50 or self.height > 50:
            return "Too big for picture."

    return ("*" * self.width + "\n") * self.height
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  def get_amount_inside(self,shape):
        width_inside = self.width // shape.width
        height_inside = self.height // shape.height
        return width_inside * height_inside

    
 # def isrectangele(self):
  #  return True
  



class Square(Rectangle):
  def __str__(self):
        # additional check to guarantee that the width and height match
        w = str(self.width)
        h = str(self.height)
        if w == h:
            return 'Square(side=' + w + ')'
        else:
            return 'Mis-shaped Square(width=' + w + ',height=' + h + ')'
  def  set_side(self,side):
    self.set_width(side)
    self.set_height(side)
  

     

