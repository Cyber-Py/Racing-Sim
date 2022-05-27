# Importing the modules
from time import sleep
import sys
import random

# Defining functions that clear the console
def clear():
  print("\033c\033[3J", end='')
def clearLA():
  sys.stdout.write("\033[F") 
  sys.stdout.write("\033[K") 

# Creating variables
XP = 100
Level = XP // 100
Coins = 100
Gems = 10
Races = 0
Car_1 = 'Lambini GT'
Car_2 = 'Grim Rod'
Car_3 = 'Dune Jumper'
Car_4 = 'Beach Buggy'
Car_5 = 'Holeshot'
EPIC_CAR = 'Micro-Ex'
Current_Car = Car_5

# Defining my typewriter function 
def printt(string, delay = 0.05):
  for i in str(string):
    print(i, end="", flush = True)
    sleep(delay)
  print('')

# Shop
def shop():
  global Coins
  global Gems
  global Current_Car
  printt('Welcome to the shop! What would you like to do today?')
  print('[1] Buy Cars\n[2] Convert Coins to Gems\n[3] Convert Gems to Coins')
  inp1 = input()
  clear()
  transaction = False
  while inp1 == '1' and not(transaction):
    print('Car Shop:\n[1] Lambini GT\n  Price: 250\n  Stats:\n    Speed: 9.2 stars\n    Toughness: 5.2 stars\n    Handling: 3.4 stars\n    Acceleration: 7.9 stars\n[2] Grim Rod\n  Price: 250\n  Stats:\n    Speed: 5.9 stars\n    Toughness: 9.7 stars\n    Handling: 5.6 stars\n    Acceleration: 4.5 stars\n[3] Dune Jumper\n  Price: 250\n  Stats:\n    Speed: 6.7 stars\n    Toughness: 6.2 stars\n    Handling: 9.6 stars\n    Acceleration: 8.5 stars\n[4] Beach Buggy\n  Price: 250\n  Stats:\n    Speed: 10.0 stars\n    Toughness: 8.7 stars\n    Handling: 4.3 stars\n    Acceleration: 0.9 stars\n')
    inp2 = input()
    if inp2 == 'exit':
      transaction = True
    elif inp2 == '1':
      if Coins - 250 < 0:
        printt('You don\'t have enough Coins')
        sleep(2)
        clear()
        sleep(2)
      else:
        Coins = Coins - 250
        transaction = True
        Current_Car = Car_1
    elif inp2 == '2':
      if Coins - 250 < 0:
        printt('You don\'t have enough Coins')
        sleep(2)
        clear()
        sleep(2)
      else:
        Coins = Coins - 250
        transaction = True
        Current_Car = Car_2
    elif inp2 == '3':
      if Coins - 250 < 0:
        printt('You don\'t have enough Coins')
        sleep(2)
        clear()
        sleep(2)
      else:
        Coins = Coins - 250
        transaction = True
        Current_Car = Car_3
    elif inp2 == '4':
      if Coins - 250 < 0:
        printt('You don\'t have enough Coins')
        sleep(2)
        clear()
        sleep(2)
      else:
        Coins = Coins - 250
        transaction = True
        Current_Car = Car_4
    else:
      printt('Input not Valid')
      clear()
    
  while inp1 == '2' and not(transaction):
    printt('How many gems do you want?')
    printt('100 coins = 1 gem')
    inp9 = input()
    transaction2 = False
    if inp9 == 'exit':
      transaction = True
      transaction2 = True
    while inp9 and not(transaction2):
      if inp9:
        Gem_TB_Converted = int(inp9) * 100
        if Coins < Gem_TB_Converted and not(transaction2) == True:
          printt('You don\'t have enough coins!')
          transaction2 = True
        elif Coins >= Gem_TB_Converted and not(transaction2) == True:
          Coins = Coins - Gem_TB_Converted
          Gems = Gems + inp9
          transaction = True
          transaction2 = True
  while inp1 == '3' and not(transaction):
    printt('How many gems do you want to convert?')
    printt('1 gem = 100 coins')
    inp10 = input()
    transaction3 = False
    if inp10 == 'exit':
      transaction = True
      transaction2 = True
      transaction3 = True
    while inp10 and not(transaction3):
      if inp10:
        Coins_TB_Converted = inp10 * 100
        if Gems < inp10 and not(transaction3) == True:
          printt('You don\'t have enough gems!')
          transaction3 = True
        elif Gems >= inp10 and not(transaction3) == True:
          Gems = Gems - inp10
          Coins = Coins + Coins_TB_Converted
          transaction = True
          transaction3 = True
  

def countdown():
  cnum = ['3','2','1']
  for i in cnum:
    printt(f'{i}...\n', 0.1)
    sleep(1)
  printt('GO', 0.1)
  sleep(2)
  clear()

def Race():
  global Races
  global XP
  global Level
  global Coins
  countdown()
  Races = Races + 1
  for i in range(11):
    if i == 1:
      print(f'{i} minute into the first lap of the race')
    elif i == 0:
      printt(f'{i} minutes into the first lap of the race')
    else:
      print(f'{i} minutes into the first lap of the race')
    sleep(1)
    clearLA()
  printt('LAP 2!')
  sleep(1)
  clearLA()
  for i in range(11):
    print(f'{i + 10} minutes into the first lap of the race')
    sleep(1)
    clearLA()
  Place = random.randint(1,6)
  clear()
  if Place == 1:
    printt(f'{Place}st place\nEarnings:\n50 XP\n30 Coins')
    XP = XP + 50
    Coins = Coins + 30
  elif Place == 2:
    printt(f'{Place}nd place\nEarnings:\n40 XP\n25 Coins')
    XP = XP + 40
    Coins = Coins + 25
  elif Place == 3:
    printt(f'{Place}rd place\nEarnings:\n30 XP\n20 Coins')
    XP = XP + 30
    Coins = Coins + 20
  else:
    printt(f'{Place}th place')
    if Place == 4:
      XP = XP + 27
      Coins = Coins + 17
      printt('Earnings:\n27 XP\n17 Coins')
    elif Place == 5:
      XP = XP + 22
      Coins = Coins + 14
      printt('Earnings:\n22 XP\n14 Coins')
    else:
      XP = XP + 16
      Coins = Coins + 10
      printt('Earnings:\n16 XP\n10 Coins')
  sleep(2)
  input()

def StheWOC(): 
  global Current_Car
  global Gems
  global Coins
  global XP
  global Level
  printt('Welcome to the Wheel of Chance')
  printt('Prizes are as follows:')
  print('1000 coins\n1000 XP\nMicro Ex (EPIC CAR)\n100 Gems\n700 coins + Second Spin')
  printt('Would you like to spin the Wheel?(600 Coins)')
  inp7 = input()
  WheelSpinFinished = False
  if Coins >= 600:
    pass
  elif Coins < 600:
    printt('You don\'t have enough Coins!')
    sleep(2)
    WheelSpinFinished = True
  while not(WheelSpinFinished):
    if inp7 == 'y' or 'yes':
      if Coins >= 600 or Gems>= 50:
        pass
      else:
        WheelSpinFinished = True
      printt('The wheel spins...')
      sleep(5)
      printt('The wheel is stopping...')
      printt('The wheel has stopped. Your prize is...')
      WSpin = random.randint(1,100)
      if WSpin <= 100 and WSpin > 90:
        printt('YOU GOT THE EPIC CAR; THE MICRO-EX')
        print('  Stats:\n    Speed: 10.0 stars\n    Toughness: 9.4 stars\n    Handling: 8.9 stars\n    Acceleration: 9.1 stars\n')
        printt('Do you want to use this car?')
        inp20 = input()
        if inp20 == 'y' or 'yes':
          Current_Car = EPIC_CAR
          WheelSpinFinished = True
        elif inp20 == 'n' or 'no':
          WheelSpinFinished = True
      elif WSpin <=90 and WSpin >50:
        printt('You got 200 coins and an extra spin!')
        Coins = Coins + 200
      elif WSpin <=50 and WSpin > 30:
        printt('You won  100 gems!')
        Gems = Gems + 100
        WheelSpinFinished = True
      elif WSpin <= 30 and WSpin > 20:
        printt('You earned 1000 XP!')
        XP = XP + 1000
        WheelSpinFinished = True
      elif WSpin <= 20 and WSpin >= 0:
        printt('You gained 1000 coins!') 
        Coins = Coins + 1000
        WheelSpinFinished = True
    else: 
      WheelSpinFinished = True

def Racing_Simulator():
  while True:
    print(f'You are at level {str(Level)} with {str(XP)}XP\nYou have ${str(Coins)}\nYou have {str(Gems)} Gems\nYour current car is: {Current_Car}\nYou have completed {str(Races)} races\n')
    print('Would you like to:\n[1] Race\n[2] Shop\n[3] Spin The Wheel Of Chance\n')
    inp = input()
    clear()
    if inp == '1':
      Race()
      clear()
    if inp == '2':
      shop()
      clear()
    if inp == '3':
      StheWOC()
      clear()




Racing_Simulator()