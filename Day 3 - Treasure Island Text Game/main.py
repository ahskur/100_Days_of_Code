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
print("Your mission is to find the treasure.")
puddle = input("You've just arrived and you're thirsty. You see a puddle of dark colored water nearby. Drink it? \nY or N: ").lower()
if puddle == ("n"):
    print("For you own good, you've decided not to drink it.")
    campfire = input("You smell fire from a distance, looking up you see smoke. Do you wish to go near the fire?\n Y or N: ").lower()
    if campfire == ("y"):
        print("You walk straight into a cannibal camp and got eaten. Bad luck!")
    else:
        print("You follow your guts and steer clear from the camp.")
        rainbow = input("After getting away from the camp you've come to a riverbed and you see a rainbow that leads to the other side. Follow it?\nY or N: ").lower()
        if rainbow == "y":
            print('''
                .##@@&&&@@##.
              ,##@&::%&&%%::&@##.
             #@&:%%000000000%%:&@#
           #@&:%00'         '00%:&@#
          #@&:%0'             '0%:&@#
         #@&:%0                 0%:&@#
        #@&:%0                   0%:&@#
        #@&:%0                   0%:&@#
        "" ' "                   " ' ""
      _oOoOoOo_                   .-.-.
     (oOoOoOoOo)                 (  :  )
      )`"""""`(                .-.`. .'.-.
     /         \              (_  '.Y.'  _)
    | #         |             (   .'|'.   )
    \           /              '-'  |  '-'
     `=========`
            ''')
            print("You've found the treasure!")
        else:
            print("The cannibals from the ealy camp catch up to you and turn you into soup while singing Bad Romance. Though luck.,")
            print('''
            .d8888b  .d88b. 888  88888888b.  
            88K     d88""88b888  888888 "88b 
            "Y8888b.888  888888  888888  888 
                 X88Y88..88PY88b 888888 d88P 
             88888P' "Y88P"  "Y8888888888P"  
                                    888      
                                    888      
                                    888           
                                    ''')
else:
    print("May God have mercy on your soul.\n YOU DIED.")

