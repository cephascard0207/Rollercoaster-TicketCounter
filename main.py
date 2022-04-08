#Rollercoaster-TicketCounter
#Created by Cephas Cardozo using Python
#Day-3 of 100DaysCodingChallenge

print("Welcome to the Rollercoaster\n")
height = int(input("What is your height in cms?\n"))
age = int(input("What is your age?\n"))

if height >= 120:
  print("You can ride the rollercoaster")

  #Nested if/else Statements
  if age <= 12:
    print("You have to pay $5")
  elif age <= 18:
    print("You have to pay $7 ")
  else:
    print("You have to pay $12")
    
else:
  print("Sorry, You cannot ride the rollercoaster")