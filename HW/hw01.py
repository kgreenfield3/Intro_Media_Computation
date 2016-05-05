# Kyrsten Greenfield
# kgreenfield@gatech.edu
# I worked on this homework assignment alone, using only this semester's course matierals

#Problem 1:
def jellyfish():
  jelly = 2.5*23
  print jelly
  
#Problem 2: 
def ufo():
  gas = 3.65*.39
  tax = gas*.07
  cost = gas + tax
  total = cost*1000
  print total

#Problem 3:
def parrot(echo):
  #str(echo) #don't need, unless you want to plug in int and floats
  print echo

#Problem 4:
def temp(cels):
  fahr = ((9*cels)/5.0) + 32
  print fahr
  
#Problem 5:
def kittyKat():
  days = 365
  cat1 = 3
  cat2 = cat1/2
  food = cat1 + cat2
  total = days*food
  print total

#Problem 6:
def kittyKat2():
  days = 365
  cat1 = 3
  cat2 = cat1/2
  food = cat1 + cat2
  cans = days*food
  NumberOfCoupons = cans/60
  full = (NumberOfCoupons*50) #number of cans paid in full
  free = NumberOfCoupons*10 #number of cans that were free
  leftovercans = cans - (full + free)#extra cans that you have to pay for
  Total = (full + leftovercans)*3 #all cans paid for in full, coupon and not
  print Total

   

  