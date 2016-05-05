#Kyrsten Greenfield
#kgreenfield@gatech.edu
#I worked on this homework assignment alone, using only this semester's course materials.

#Problem 1:
def paintPic(pic):
  for each in getPixels(pic):   
   r = getRed(each)
   g = getGreen(each)
   b = getBlue(each)
   if r > 100:
     setRed(each, 255)
   if r < 100:
     setRed(each, 0)
   if g > 100:
     setGreen(each, 255)
   if g < 100:
     setGreen(each, 0)
   if b > 100:
     setBlue(each, 255) 
   if b < 100:
     setBlue(each, 0)    
  show(pic)

#Problem 2:
def border(size, col, pic):
  for each in getPixels(pic):
    r = getRed(each)
    g = getGreen(each)
    b = getBlue(each)
    if 0 <= getX(each) < size:
      setColor(each, col)
    if (getWidth(pic) - size) < getX(each) < getWidth(pic):
      setColor(each, col)
    if 0 <= getY(each) < size:
      setColor(each, col)  
    if (getHeight(pic)-size) < getY(each) < getHeight(pic):
      setColor(each, col)  
  show(pic)
 
#Problem 3:  
def helpMeOut(pic):
  for each in getPixels(pic):
   r = getRed(each)
   g = getGreen(each)
   b = getBlue(each)
   if white:
     setColor(each, black)
   if r > 180:
     setColor(each, red) 
   if r < 180:
     setColor(each, black)  
     if b > 180:
       setColor(each, blue)
     if b < 180:
       setColor(each, black)
       if g > 180:
         setColor(each, green)
       if g < 180:
         setColor(each, black)
  show(pic)
 
#Problem 4:   
def pinker(pic):
  for each in getPixels(pic):
    r = getRed(each)
    g = getGreen(each)
    b = getBlue(each)
    if r and g and b >= 100:
      setColor(each, pink)
    if r < 100:
      setRed(each, r)
    if g < 100:
      setGreen(each, g)
    if b < 100:
      setBlue(each, b)
  show(pic)
  