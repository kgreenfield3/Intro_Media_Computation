#Kyrsten Greenfield
#kgreenfield@gatech.edu
#I worked on this homework assignment alone, using only this semester's course materials.

#Problem 1:
def screen(pic, color, threshold, newColor):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      pixel = getPixels(pic, x,y)
      origColor = getColor(pixel)
      if distance(origColor, color) < threshold:
        setColor(pixel, newColor)
  show(pic)

#Problem 2:
def flip(pic):
  canvas = makeEmptyPicture(getHeight(pic), getWidth(pic))
  targetX=1
  for sourceX in range(1,getWidth(pic)):
    targetY=1
    for sourceY in range(1,getHeight(pic)):
      color=getColor(getPixel(pic,sourceX,sourceY))
      setColor(getPixel(canvas,targetY,targetX),color)
      targetY=targetY+1
    targetX=targetX+1
  for each in getPixels(canvas):
    r = getRed(each)
    g = getGreen(each)
    b = getBlue(each)
    if g < 100:
      setColor(each, black)
  return canvas

#Problem 3:
def doubleMirror(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  canvas = makeEmptyPicture(w*2, h)
  for x in range(0, w):
    for y in range(0, h):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas, w*2-x-1, y), color)
  mirrorpoint = int(getHeight(canvas)/2)
  for y in range(1,mirrorpoint):
    for x in range(1,getWidth(canvas)):
      bottom = getPixel(canvas,x,y+mirrorpoint)
      top = getPixel(canvas,x,mirrorpoint-y)
      setColor(bottom,getColor(top))
  show(canvas)

#Problem 4:
def peekAKitty(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  canvas = makeEmptyPicture(w, h)
  for x in range(0, w):
    for y in range(0, h):   
      startX = 0
      startY = 0
      if x >= y:
        OrigPic = getPixel(pic,x, y)
        newPic = getPixel(canvas, x+startX, y+startY)
        color = getColor(OrigPic)
        setColor(newPic, color)
  show(canvas)

#Problem 5:
def edge(pic):
  canvas = makeEmptyPicture(getWidth(pic),getHeight(pic))
  for x in range(0, getWidth(pic)-1):
    for y in range(0, getHeight(pic)-1):
      origPix = getPixel(pic, x, y)
      neighborPix = getPixel(pic, x+1, y+1)
      newPix = getPixel(canvas, x, y) 
      origLum = (getRed(origPix) + getGreen(origPix) + getBlue(origPix)) 
      neighborLum = (getRed(neighborPix) + getGreen(neighborPix) + getBlue(neighborPix)) 
      neighborDiff = abs(origLum - neighborLum)
      setColor(newPix, makeColor(neighborDiff))
  show(canvas)
  
#Problem 6:
def makeCollage():
  pic = makePicture(getMediaPath("flower2.jpg"))
  canvas=makeEmptyPicture(800, 600) 
  targetX=50
  for sourceX in range(1,getWidth(pic)): #orginal 
    targetY=getHeight(canvas)-getHeight(pic) -300
    for sourceY in range(1,getHeight(pic)):
      px=getPixel(pic,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  allpixels = getPixels(pic) #blackout
  for index in range(0, len(allpixels)/2):
    pixel = allpixels[index]
    setColor(pixel, green)
  targetX=175
  for sourceX in range(1,getWidth(pic)):
    targetY=getHeight(canvas)-getHeight(pic) -300
    for sourceY in range(1,getHeight(pic)):
      px=getPixel(pic,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  for px in getPixels(pic): #neg and blackout
    r = getRed(px)
    g = getGreen(px)
    b = getBlue(px)
    neg = makeColor(255-r, 255-g, 255-b)
    setColor(px, neg)
  targetX=300
  for sourceX in range(1,getWidth(pic)):
    targetY=getHeight(canvas)-getHeight(pic) -300
    for sourceY in range(1,getHeight(pic)):
      px=getPixel(pic,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  mirrorpoint = int(getHeight(canvas)/2) #top-to-bottom mirror
  for y in range(1,mirrorpoint):
    for x in range(1,getWidth(canvas)):
      bottom = getPixel(canvas,x,y+mirrorpoint)
      top = getPixel(canvas,x,mirrorpoint-y)
      setColor(bottom,getColor(top))
  mirrorpoint = int(getWidth(canvas)/2) #left-to-right mirror 
  for y in range(1,getHeight(canvas)):
    for x in range(1,mirrorpoint):
      right = getPixel(canvas, x+mirrorpoint,y)
      left = getPixel(canvas, mirrorpoint-x,y)
      c = getColor(left)
      setColor(right,c)
  return canvas

