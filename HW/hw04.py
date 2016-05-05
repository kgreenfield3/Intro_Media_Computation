#Kyrsten Greenfield
#kgreenfield@gatech.edu  
#I worked on this homework assignment alone, using only this semester's course materials.

#Problem 1:
def goose(list):
  for name in range(0, len(list), 4):
    print list[name] + " " + "is the goose!"

#Problem 2:    
def thisTall(personList, rideList):
 for index in range(len(rideList)):
   if (rideList[index] >= 44):
     print personList[index] + " " + "can ride!"
     
#Problem 3:     
def grade(gradeNum):
   if (gradeNum >= 90):
    return "A"
   if (gradeNum >= 80):
    return "B" 
   if (gradeNum >= 70):
    return "C" 
   if (gradeNum >= 60):
    return "D" 
   if (gradeNum < 60):
    return "F" 

#Problem 4:
def lineSwap(lineList):
  lineList[0], lineList[2] = lineList[2], lineList[0]
  print lineList
  

 
 
 

   

 
    
  


  