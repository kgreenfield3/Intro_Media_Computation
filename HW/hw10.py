#Kyrsten Greenfield
#kgreenfield@gatech.edu
#I worked on this homework assignment alone, using only this semester's course materials.

#Problem 1:
def tellMe(dir, question):
  file = open(dir + "tellMe.txt", "wt")
  file.write("""How tall is a cat? Not very.    
How tall is Mt. Everest? 29,029 ft. 
What is your name? Perhaps Susie.""")
  file.close()
  file = open(getMediaPath("tellMe.txt"),"rt")
  contents = file.readlines()
  for each in contents:
    start = each.rfind(question)
    end = each.rfind("\n")
    if start > -1:
      start = each.rfind("?")
      end = each.rfind(".")
      if start > -1:
        answer = each[start + 2: end]
        print answer
  file.close() 
   
#Problem 2:
def whatLine(name): #this is very ugly code, but it works
  file = open("C:\\Users\\Kyrsten\\Desktop\\name.txt","wt")
  file.write("Brett" + "\n" + "Jessica" + "\n" + "Kelsey" + "\n" + "Mike" + "\n" + "Heather" + "\n" + "Lindsay" + "\n" + "Robert" + "\n" + "Thomas" + "\n" + "Barabara" + "\n" + "Kristen" + "\n" + "Jillian" + "\n" + "William" + "\n" + "Amanda" + "\n" + "Jeff" + "\n" + "Robert")
  file.close()
  file = open(getMediaPath("name.txt"),"rt")
  read = file.read()
  first = read.split().index(name)
  print str(first + 1)
  file.close()
  file = open(getMediaPath("name.txt"),"rt")
  if name == "Robert":
    second = file.readlines().index(name)
    print str(second + 1)
  file.close()
  
#Problem 3:
def generator(path, filename): #path = setMediaPath(images2 from CS)
  output = open(dir + filename,"wt")
  output.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">')
  output.write("<html><head><title>" +"Pictures for CS 1315" + "</title></head>");
  bodyString = "" 
  for file in os.listdir(dir):
    if file.endswith(".jpg"):
      bodyString = bodyString + '<td><image src="' + dir  + file+'" width="100" height = "100"/></td>'
      bodyString = bodyString + "</td><td>"
  output.write("<body>" + bodyString + "</body></html>")
  output.close() 
