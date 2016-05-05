# Kyrsten Greenfield
# kgreenfield@gatech.edu
# I worked on this homework assignment alone, using only this semester's course matierals

def newt(): #new turtle
  earth = makeWorld()
  w = makeTurtle(earth)
  return w

#Problem 1:
def factorialFun(int):
  print "The factorial of" + " " + str(int) + " " + "is" + " " + str(fact(int)) + "."

def fact(int):
   if int == 0 or int == 1:
    factorial = 1
    return factorial
   factorial = int*fact(int - 1)
   return factorial
   
#Problem 2:  
def shell(turtle, lineLength):
  if lineLength <= 0:
    return 
  turtle.forward(int(lineLength))
  turtle.turn(45)
  shell(turtle, lineLength -5)

#Problem 3: #does dist = 150? #dist = 75 matches the test case
def line(distance, turtle):
  if distance <= 0:
    return
  turtle.forward(5)
  turtle.penUp()
  turtle.forward(5)
  turtle.penDown()
  sleep(.5)
  line(distance-5, turtle)
  
#Problem 4:
def tSquare(t, num): #matches the instructions
  if num <= 0:
    return
  t.forward(num)
  t.turn(90)
  tSquare(t, num-1)

def tSquare1(t, num): #matches the test case
  if num <= 0:
    return
  t.turn(90)
  t.backward(num)
  tSquare(t, num-1)

#Problem 5:
import time 
from time import sleep
def sky():
  earth = makeWorld()
  w = makeTurtle(earth)
  star(w, 50, 10)
  w.penUp()
  w.forward(100) 
  
def star(w, side, counter):
  if counter <= 0:
    return
  if counter == 0:
    w.turn(18)
  if counter%2 != 0:
   w.turn(162)
  w.forward(side)
  sleep(.5)
  star(w, side, counter -1)
  
 
  
  
  