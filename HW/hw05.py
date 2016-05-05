#Kyrsten Greenfield
#kgreenfield@gatech.edu
#I worked on this homework assignment alone, using only this semester's course materials.

#Problem 1:
def seeBlue(pic):
  for each in getPixels(pic):   
   r = (getRed(each))/2.0
   g = (getGreen(each))/2.0
   b = (getBlue(each))*2.0
   setRed(each, r)
   setGreen(each, g)  
   if b > 255:
     setBlue(each, 255) 
   if b < 255:
     setBlue(each, b)    
  show(pic)

#Problem 2: 
def wizard():
  HP = makePicture(getMediaPath("dumbledore.jpg"))
  LOTR = makePicture(getMediaPath("gandalf.jpg"))
  for x in range(1, getWidth(LOTR)): 
    for y in range(1, getHeight(LOTR)/2): 
      pix1 = getPixel(LOTR,x,y) 
      pix2 = getPixel(HP,x,y) 
      setColor(pix1,getColor(pix2))
  show(LOTR, HP)
    
#Problem 3:
def three(pic):
  for each in getPixels(pic):
    r = getRed(each)
    g = getGreen(each)
    b = getBlue(each)
    lum = (r+g+b)/3.0
    if lum < 85:
      setColor(each, blue)
    if lum > 86 and lum < 170:
      setColor(each, green)
    if lum > 170:
      setColor(each, red)
  show(pic)

#Problem 4:   
def onlyBlue(pic):
  for each in getPixels(pic):
    r = getRed(each)
    g = getGreen(each)
    b = getBlue(each) 
    setRed(each, r)
    setGreen(each, g)
    if b < 155:
      setColor(each, white)
    if b >= 155:
      setBlue(each, b)
  show(pic)

#Problem 5:
def blackout(pic):
  pixels = getPixels(pic)
  for index in range(0, len(pixels)/2):
     pixel = pixels[index]
     setColor(pixel,black)
  show(pic)

#Problem 6:
def brightenGrey(pic):
  for each in getPixels(pic):
    r = getRed(each) + 100
    g = getGreen(each) + 100
    b = getBlue(each) + 100
    lum = (r+g+b)/3.0
    setRed(each, lum)
    setGreen(each, lum)
    setBlue(each, lum)
  show(pic)
    
      
    
  