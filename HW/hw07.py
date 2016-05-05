#Kyrsten Greenfield
#kgreenfield@gatech.edu
#I worked on this homework assignment alone, using only this semester's course materials.

#Problem 1:
def bars(pic, size):
  w = getWidth(pic)
  h = getHeight(pic)
  for x in range(0, size):
    for y in range(0,h):
      pix = getPixelAt(pic, x, y)
      setColor(pix, black)
  for x in range((w/2) - (size/2), (w/2) + (size/2)):
    for y in range(0,h):
      pix = getPixelAt(pic, x, y)
      setColor(pix, black)
  for x in range(w - size, w):
    for y in range(0,h):
      pix = getPixelAt(pic, x, y)
      setColor(pix, black)      
  show(pic)

#Problem 2:
def mirror(pic):
  targetX = getWidth(pic) -1
  for sourceX in range(0, getWidth(pic)/2):
    targetY = 0
    for sourceY in range(0, getHeight(pic)):
      mypixel = getPixelAt(pic, sourceX, sourceY)
      color = getColor(mypixel)
      newpixel = getPixelAt(pic, targetX, targetY)
      setColor(newpixel, color)
      targetY = targetY + 1
    targetX = targetX - 1
  show(pic)

#Problem 3:
def halfsies(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  for x in range(0, w/2):
    for y in range(0, h):
      pix = getPixelAt(pic, x, y)
      r = getRed(pix) + 100
      g = getGreen(pix) + 100
      b = getBlue(pix) + 100
      setRed(pix, r)
      setGreen(pix, g)
      setBlue(pix, b)
  for x in range(w/2, w):
    for y in range(0, h):
      pix = getPixelAt(pic, x, y)
      r = getRed(pix) 
      g = getGreen(pix) 
      b = getBlue(pix)
      lum = (r+g+b)/3
      setRed(pix, lum)
      setGreen(pix, lum)
      setBlue(pix, lum)
  show(pic)

#Problem 4:
def thirds(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  for x in range(0, w):
    for y in range(0, h/3):
      pix = getPixelAt(pic, x, y)
      r = getRed(pix) + 100
      g = getGreen(pix) + 100
      b = getBlue(pix) + 100
      setRed(pix, r)
      setGreen(pix, g)
      setBlue(pix, b)
  for x in range(0, w):
    for y in range((2*h)/3, h):
      pix = getPixelAt(pic, x, y)
      r = getRed(pix) + 150
      g = getGreen(pix) 
      b = getBlue(pix)
      setRed(pix, r)
      setGreen(pix, g)
      setBlue(pix, b)
  show(pic)

#Problem 5:
def snowflake():
  pic = makeEmptyPicture(255, 255)
  for each in getPixels(pic):
    addLine(pic, getWidth(pic)/2, 0, getWidth(pic)/2, 255)
    addLine(pic, 0, getHeight(pic)/2, 255, getHeight(pic)/2)
    addLine(pic, 0, 255, 255, 0)
    addLine(pic, 0,0,255,255)
  show(pic)
