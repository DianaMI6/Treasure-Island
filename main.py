print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure before sunset.") 

decision1 = input("\n\nYou arrive at Treasure Island!\n\nYou get off the ship and scout the area:\nThere is a jungle right in front of you. You could go there, or simply wander along the coast.\nWhere do you want to go?\nType 'jungle' or 'coast'.\n").lower()

if decision1 == "jungle":
  decision2 = input("\nAs you venture deeper into the misty woods, the clashing of ocean waves fades. You hear birds singing, wings fluttering and monkeys shrieking.\nYou find a ravine with a gushing stream many meters below. Vines hang down from the thick canopy. To the right you see a narrow path alongside the ravine.\nYou could swing to the other side of the ravine by using one of the vines to your left; or you could take the path to your right.\nWhich way do you want to go? Type 'left' or 'right'.\n").lower()
  
  if decision2 == "right":
    decision3 = input("\nThe path brings you to a glade with downed trees and dense undergrowth. The glazing sun reveals three colored cave entrances: red, blue and green.\nWhich cave do you want to explore? Type 'red', 'blue' or 'green'.\n").lower()    
    if decision3 == "red":
      print("\nYou enter the cave which appears to have blood stains at the walls. You see a pair of glowing, amber eyes looking straight at you from the darkness of the cave. The beast's terrifying growl makes you tremble. You run for your life and miraculously reach the safety of your ship - empty-handed.\nGAME OVER.")
    elif decision3 == "blue":
      print("\nYou enter the cave that becomes steeper the deeper you go - until you slip and fall into a never-ending void.\nGAME OVER.")
    elif decision3 == "green":
      print("\nThe cave leads you to a big room, decorated with precious tapestries and golden lampstands. In the middle you find the huge legendary chest of Treasure Island.\nYou win!")
      print('''                   \       /            _\/_
                     .-'-.              //o\  _\/_
  _  ___  __  _ --_ /     \ _--_ __  __ _ | __/o\\ _
=-=-_=-=-_=-=_=-_= -=======- = =-=_=-=_,-'|"'""-|-,_ 
 =- _=-=-_=- _=-= _--=====- _=-=_-_,-"          |
jgs=- =- =-= =- = -  -===- -= - ."''')
    else:
      print("\n\nYou look to be indecisive. What a pity! You stand and look around, the sun goes down, the ship leaves, and you're still there...\nGAME OVER.")
      
  else:
    print("\nYou grab a vine and start swinging, but you miscalculated your strength and the wide gap - you fall. Fortunately, you get washed up back ashore on time, just before the sun sets and your ship departs.\nYou leave Treasure Island with empty hands...\n\n\nGAME OVER.")
     
else:
  print("\nYou walk along the shore. Sunset is near - but you still find no hints for any treasure.\n\nYour crew calls you back to the ship; you leave Treasure Island with empty hands...\n\n\n")
  print('''            ^^                   @@@@@@@@@
       ^^       ^^            @@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@              ^^
                           @@@@@@@@@@@@@@@@@@@@
 ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
 ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
   ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~
   ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~
 ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
       ~             ~        ~      ~      ~~   ~             ~''')