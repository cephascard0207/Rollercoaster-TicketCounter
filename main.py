#Rollercoaster-TicketCounter
#Created by Cephas Cardozo using Python
#Day-3 of 100DaysCodingChallenge

print("Welcome to the Rollercoaster\n")
height = int(input("What is your height in cms?\n"))
age = int(input("What is your age?\n"))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster")

  #Nested if/else Statements
  if age <= 12:
    bill = 5
    print("You have to pay $5")
  elif age <= 18:
    bill = 7 
    print("You have to pay $7 ")
  elif age >= 45 and age <= 55:
    print("Everything is gonna be OK. Have a free Ride")
  else:
    bill = 12
    print("You have to pay $12")

  wants_photo = input("Do you want a photo? Y or N\n")
  if wants_photo == "Y":
    bill += 3
  print(f"Your bill is ${bill}")
  
else:
  print("Sorry, You cannot ride the rollercoaster")