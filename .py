print('''
____________________________________________________
|,---.        ) ALT.PEEVES of USENET (          ,---.|
|) 1 (        `====---    _   ---===='          ) 1 (|
| \ /                    | |                     \ / |
|  V      ,-.            |-|                      V  |
|        ( D )          _|-|_         good  for      |
|         `-'         _(_) (_)         O  N  E       |
|                    (_) | | L_.       c-l-u-e       |
|      M21141815E    '      (_  \                    |
| / \               (        /  /                / \ |
|( 1 )                                          ( 1 )|
| \ / ---==<  E L E C T R O D O L L A R  >==---  \ / |
|____________________________________________________|
''')

print("Welcome to Money Island.")
print("Your mission is to find the hidden cash.") 
print("You started running down a path and it was split into two roads. The right road was full of flowers with a sunny nice weather and free cocktails at the end, the left road was buried with snow, it was so cold that even the wind had blown away your hat just by looking in its direction, and it was said to be filled with silver wolves....")

first_route = input("Which road will you take? Left or Right? ").lower()
is_dead = False
while not is_dead:
    if first_route == 'right':
        print("You got stuck at the bar, got addicted to free cocktails, forgot your task and one day died from liver failure.")
        is_dead = True
        exit()
    if first_route == 'left': 
        print("You walked down the tough route, fighting cold and hunger for days. You notice a glimpse of a fire and run towards it seeking refuge or help, only to be surprised by the myth of the silver wolves! You have the option to shoot the wolves or offer them companionship.")
        wolf_choice = input("What will you do? Kill or befriend? ").lower()
        if wolf_choice == 'kill':
            print("The wolves were quicker to snatch you and you turned into their dinner tonight. Game over.")
            is_dead = True
            exit()
        elif wolf_choice == 'befriend':
            print("They invited you to dinner and in the morning, they took you on their backs to the end of the cold forest, gave you a map, water, and extra food.")
            print("After you said goodbye to your wolf pack, and started walking, you notice there's an end of daily boat cruise?")
    choice_2 = input("Swim or Wait? ").lower()
    if choice_2 == 'swim':
        print("You got eaten by a shark, only your shorts on the surface of the water were left to celebrate your long-lost existence. Game over.")
        is_dead = True
        exit()
    if choice_2 == 'wait':
        print("You got greeted by a small wooden made boat that offered you a free ride, 10 hour sleep and great traditional Lebanese breakfast.")
        print("An hour after searching around the island you walk into a huge caste-like building, where you're greeted with 3 doors, each door has a different language with a quote on it.")
        print("RED DOOR: HAD A FRENCH QUOTE 'CROIS EN TOI' which means 'believe in yourself' \n YELLOW DOOR: HAD A SPANISH QUOTE 'APRENDI A VIVIR' which means 'I learned to live' \n BLUE DOOR: HAD AN ARABIC QUOTE 'اعتز بحياتك' which means be proud of your life'")
door_choice = input("Which door will you choose? Red, Yellow, or Blue? ").lower()
if door_choice == 'red':
 print("You walked into a room full of self-help books and motivational speakers, you spent the next few years of your life learning and developing yourself, but you never found the hidden cash. The End")
exit()
if door_choice == 'yellow':
 print("You walked into a room full of art and music, you spent the next few years of your life creating and enjoying, but you never found the hidden cash. The End")
exit()
if door_choice == 'blue':
 print("You walked into a room full of money, gold, and jewels, you finally found the hidden cash! Congratulations, You Win!")
exit()
