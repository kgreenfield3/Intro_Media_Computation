#Kyrsten Greenfield
#kgreenfield@gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials 

#Problem 1:
def castNet(name, day, num): 
  string1 = "won the contest with a great catch of"
  string2 = 'fish on'
  string3 = '!'
  num2 = str(num)
  print name + " " + string1 + " " + num2 + " " + string2 + " " + day +  string3

#Problem 2:
def icecream(students):
  cones = 7.5
  gallons = (students*cones)
  print int(gallons)

#Problem 3:
def baker(flavor1, flavor2):
  string = ""
  for index in range(0, len(flavor1)/2):
    string = string + flavor1[index]
  for index in range(len(flavor2)/2, len(flavor2)):
    string = string + flavor2[index]
  print string
  
#Problem 4:   
def crown(s):
  print "     " +  " " + s + "        " + s + "        " + s + "\n" + "   " + s + s + s + "    " + s + s + s + "    " + s + s + s + "    " + "\n" + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + "\n" + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + "\n"

#Problem 5:
def space(message):
  string = ""
  for index in range(0, len(message)):
    string = string + message[index] + " "
  print string

#Problem 6:
def mcdonalds(cusNum, num, food, extra):
  string1 = "Customer number"
  string2 = 'wants'
  string3 = 'with extra'
  string4 = '.'
  cusNum2 = str(cusNum)
  num2 = str(num)
  print string1 + " " + cusNum2 + " " + string2 + " " + num2 + " " + food + " " + string3 + " " + extra + string4

#Problem 7: 
def sandwiched(word1, word2):
  string = "" 
  for index in range(0, (len(word1)/2)):
    string = string + word1[index] 
  string = string + " "
  for index in range(0, len(word2)):
    string = string + word2[index] 
  string = string + " "
  for index in range(len(word1)/2, len(word1)):
    string = string + word1[index] 
  print string
    

  
