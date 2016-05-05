#Kyrsten Greenfield
#kgreenfield@gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials

#Problem 1:
def pizza(nameList):
  for name in range(len(nameList)):
    print nameList[name] + " " + "wants pizza!"

#Problem 2:
def sleep(napTime, alarm):
   hourList = range(napTime, alarm)
   return hourList

#Problem 3:   
def reverse(message):
  x = " "
  for letter in message:
   x = letter + x
  print x

#Problem 4: 
def oddSum(num): 
 sum = 0
 numbers = range(1, (num+1), 2) #range will be 1 to num 
 for number in numbers:
   sum = sum + number
 return sum

#Problem 5:  
def blastOff(num):
  for x in range(num, 0, -1):
    print x
  print "Blast Off!"

#Problem 6:
def theNextRound(contestants):
  for name in range(0, len(contestants), 3):
    print contestants[name] + " " + "can continue to the next round!"

#Problem 7: 
def planner(days, events):
  for index in range(0, len(days)):
   print days[index] +  ":" + " " + events[index]
  
   
    
     
 
   
 
 
  
