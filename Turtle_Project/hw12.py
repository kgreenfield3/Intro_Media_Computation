# Kyrsten Greenfield
# kgreenfield@gatech.edu
# I worked on this homework assignment alone, using only this semester's course matierals

#Animation Description:
  #This program show a redramatization of Ted the turtle's abduction.
  #That night, Ted was heading home late.
  #According to Ted, the forest was quiet that night.
  #Ted only remembers hearing Frank the frog making some noise.
  #As Ted got closer to his home, he recalls being watched.
  #Ted could see a figure in the treeline, just staring at him as he got back to his log located in the bushes.
  #Little did Ted know that this figure was an alien, whose ship was right above Ted's house.
  #Once Ted got into his home, he recalls seeing three bright beams of light.
  #The lights grabbed him and pulled him out of his house.
  #Before he knew it, Ted was floating towards an UFO! 

#Extra Credit:
  #I used recursion in the lineCenter, lineLeft, and lineRight functions.
  
#Turtle Debut:
import time 
from time import sleep
def animateTurtles():
  earth = makeWorld(500, 500)
  t1 = makeTurtle(earth)
  spaceShip(t1, 13)
  t2 = makeTurtle(earth)
  spaceShip1(t2)
  t7 = makeTurtle(earth)
  alien(t7)
  frog = makeSound("croak.wav")
  blockingPlay(frog)  
  s = makeSound("theme.wav")
  play(s)
  t3 = makeTurtle(earth)
  movingAround(t3)
  t4 = makeTurtle(earth)
  t4.penUp()
  t4.hide()
  t4.moveTo(252, 120)
  t4.turn(180)
  t4.penDown()
  lineCenter(125, t4)
  t5 = makeTurtle(earth)
  t5.penUp()
  t5.hide()
  t5.moveTo(252, 120)
  t5.turn(200)
  t5.penDown()
  lineLeft(125, t5)
  t6 = makeTurtle(earth)
  t6.penUp()
  t6.hide()
  t6.moveTo(252, 120)
  t6.turn(160)
  t6.penDown()
  lineRight(125, t6)
  t3 = makeTurtle(earth)
  abduction(t3)
  t4.clearPath()
  t5.clearPath()
  t6.clearPath()
  sleep(.5)
  play(flip(frog))
   
def flip(s):
  sample = getSamples(s)
  returnSound = makeEmptySound(len(sample))
  returnSample = getSamples(returnSound)
  returnIndex = len(returnSample) - 1
  for index in range(0, len(sample)):
    value = getSampleValue(sample[index])
    setSampleValue(returnSample[returnIndex], value)
    returnIndex = returnIndex -1
  return returnSound 
  
def spaceShip(t1, size):
  t1.penUp()
  t1.hide()
  t1.moveTo(0,0)
  picture = makePicture(getMediaPath("Forest.jpg"))
  t1.drop(picture)
  t1.setPenColor(gray)
  t1.setPenWidth(5)
  t1.penUp()
  t1.moveTo(200, 75)
  t1.penDown()
  for n in range(size):
    t1.forward(35)
    t1.turn(36)
    
def spaceShip1(t2):
  t2.setColor(gray)
  t2.hide()
  t2.setPenWidth(5)
  t2.penUp()
  t2.moveTo(200, 40)
  t2.turn(-100)
  t2.penDown()  
  t2.forward(100)
  t2.turn(-160)
  t2.forward(80)
  t2.turn(-10)
  t2.forward(140)
  t2.turn(-10)
  t2.forward(80)
  t2.turn(-160)
  t2.forward(95)

def movingAround(t3): 
  t3.setShellColor(blue)
  t3.setBodyColor(white)
  t3.penUp()
  t3.moveTo(50,475)
  sleep(.75)
  t3.forward(25)
  sleep(.75)
  t3.turn(15)
  sleep(.75)
  t3.forward(25)
  sleep(.75)
  t3.forward(20)
  sleep(.75)
  t3.turn(30)
  sleep(.75)
  t3.turn(35)
  sleep(.75)
  t3.forward(25)
  sleep(.75)
  t3.forward(20)
  sleep(.75)
  t3.forward(30)
  sleep(.75)
  t3.forward(20)
  sleep(.75)
  t3.forward(20)
  sleep(.75)
  t3.forward(25)
  sleep(.75)
  t3.turn(15)
  sleep(.75)
  t3.forward(35)
  sleep(.75)
  t3.forward(25)
  t3.hide()

def lineCenter(distance, t4):
  if distance <= 0:
    return
  t4.setColor(yellow)
  t4.setPenWidth(3)
  t4.forward(5)
  t4.penUp()
  t4.forward(5)
  t4.penDown()
  sleep(.05)
  lineCenter(distance-5, t4)

def lineLeft(distance, t5):
  if distance <= 0:
    return
  t5.setColor(yellow)
  t5.setPenWidth(3)
  t5.forward(5)
  t5.penUp()
  t5.forward(5)
  t5.penDown()
  sleep(.05)
  lineLeft(distance-5, t5)
  
def lineRight(distance, t6):
  if distance <= 0:
    return
  t6.setColor(yellow)
  t6.setPenWidth(3)
  t6.forward(5)
  t6.penUp()
  t6.forward(5)
  t6.penDown()
  sleep(.05)
  lineRight(distance-5, t6)
 
def abduction(t3):
  t3.hide()
  sleep(1.0)
  t3.setShellColor(blue)
  t3.setBodyColor(white)
  t3.penUp()
  t3.moveTo(252, 380)
  t3.show()
  t3.forward(35)
  sleep(.75)
  t3.forward(35)
  sleep(.75)
  t3.forward(35)
  sleep(.75)
  t3.forward(35)
  sleep(.75)
  t3.forward(35)
  sleep(.75)
  t3.forward(35)
  sleep(.75)
  t3.forward(35)
  t3.hide()

def alien(t7):
  t7.hide()
  t7.penUp()
  t7.setShellColor(green)
  t7.setBodyColor(green)
  t7.setWidth(10)
  t7.setHeight(40)
  t7.moveTo(420,380)
  t7.show()





  
  
 
