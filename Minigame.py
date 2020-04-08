import random
import sys
from time import *

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'My sources say no', 'Outlook not so good', 'Very doubtful']
def Magic8Ball():
    print('What is your question? (N to quit) ')
    print()
    reply = input()
    if reply == "N":
        exit()
    else:
        print(reply)
        print (answers[random.randint(0, len(answers)-1)] )
        print()
        Replay()
    
def Replay():
    Magic8Ball()

def Jokes():
    for x in range(1):
        print("Your random number is:", random.randint(1,101))


def madlibs():
    adjective1=input("type an adjective: ")
    adjective2=input("type an adjective: ")
    noun1=input("type a noun: ")
    noun2=input("type a noun: ")
    pluralnoun1=input("type a plural noun: ")
    game=input("name a game: ")
    pluralnoun2=input("type a plural noun: ")
    verb1=input("type a verb ending in 'ing': ")
    verb2=input("type a verb ending in 'ing': ")
    pluralnoun3=input("type a plural noun: ")
    verb3=input("type a verb ending in 'ing': ")
    noun3=input("type a noun: ")
    plant=input("name a type of plant: ")
    partofbody=input("name a body part: ")
    place=input("name a place: ")
    verb4=input("type a verb ending in 'ing': ")
    adjective3=input("name a adjective: ")
    number=input("type a number: ")
    pluralnoun4=input("type a plural noun: ")
    print()
    print("A vacation is when you take a trip to some", adjective1, "place with your", adjective2, "family.\nUsually you go to some place that is near a/an", noun1, "or up on a/an", noun2,".\nA good vacation place is one where you can ride", pluralnoun1, "or play", game,"or go hunting for",pluralnoun2,".\nI like to spend my time", verb1, "or", verb2,".\nWhen parents go on vacation, they spend their time eating three", pluralnoun3, "a day, and fathers play golf, and mothers sit around", verb3,".\nLast summer, my little brother fell in a/an", noun3, "and got poison", plant, "all over his", partofbody,".\nMy family is going to go to the", place, ", and I will practice" ,verb4,".\nParents need vacations more than kids because parents are always very", adjective3, "and because they have to work", number,"hours every day all year making enough", pluralnoun4, "to pay for the vacation.")

def madlibs2():
    place1=input("type a place: ")
    adjective1=input("type an adjective: ")
    femalecel=input("type a female celebrity: ")
    bodypart1=input("type a body part: ")
    bodypart2=input("type a body part: ")
    organ=input("type a human organ: ")
    adjective2=input("type an adjective: ")
    malecel=input("type a male celebrity: ")
    adjective3=input("type an adjective: ")
    bodypart3=input("type a body part: ")
    bodypart4=input("type a body part: ")
    place2=input("type a place: ")
    celebrity=input("type a celebrity: ")
    animal=input("type an animal: ")
    verb=input("type a verb: ")
    number=input("type a number: ")
    bodypart5=input("type a body part: ")
    adjective4=input("type an adjective: ")
    adjective5=input("type an adjective: ")
    pastverb=input("type a past tense verb: ")
    print()
    print("Once upon a time, in a place called", place1, "there was a", adjective1, "princess named", femalecel, ". Her kindgom was huge, but her", bodypart1, "was bigger. She was beautiful from her", bodypart2, "to her", organ, ". One day she saw a", adjective2, "prince named", malecel, ". He had a", adjective3, "face. As soon as his", bodypart3, "touched her", bodypart4, "they fell in love. They got married at", place2,"the following day. Not long after, they had a baby. They decided to call him/her", celebrity, "He/she looked like a", animal, ". He/she used to", verb, number, "times a day so that his/her", bodypart5, "would be", adjective4, "and", adjective5, ". And they", pastverb, "happily ever after!")

def madlibs3():
    adjective1=input("type an adjective: ")
    adjective2=input("type an adjective: ")
    bodypart1=input("type a body part: ")   
    noun1=input("type a noun: ")
    animal=input("type an animal: ")
    verb1=input("type a verb: ")
    adverb1=input("type an adverb: ")
    noun2=input("type a noun: ")
    adjective3=input("type an adjective: ")
    noun3=input("type a noun: ")
    verb2=input("type a verb: ")
    noun4=input("type a noun: ")
    bodypart2=input("type a body part: ")
    noun5=input("type a noun: ")
    adverb2=input("type an adverb: ")
    verb3=input("type a verb: ")
    verb4=input("type a verb: ")
    exclamation=input("type an exclamation: ")
    pastverb1=input("type a past tense verb: ")
    pastverb2=input("type a past tense verb: ")
    number1=input("type a number: ")
    number2=input("type a number: ")
    verb5=input("type a verb: ")
    verb6=input("type a verb: ")
    verb7=input("type a verb: ")
    adverb3=input("type an adverb: ")
    print()
    print("When we first met, you looked", adjective1, "and", adjective2, ". I couldn't believe my", bodypart1, "You smelled like", noun1, "and walked as graceful as a", animal, ". I couldn't wait to", verb1, "to you. I", adverb1, "asked you if I could have your", noun2, ". I could see a look of", adjective3, "in your eyes. You hesitated for a moment, then gave me a", noun3,". I finally got to take you on our first date. I loved spending time with you. You could make me", verb2, "so easily, like no one had before. When you touched me, I felt", noun4, "up to my", bodypart2, ". When you looked at me, I could see", noun5, ". I knew we were meant to be together. After a", adverb2, "night. I was so", verb3, "to bring you home. I longed to", verb4, "you again. You looked at me and said", exclamation, "and I just knew. You", pastverb1, "me and I", pastverb2, "you. Here we are after all this time. It feels like it has been", number1, "years! I look forward to", number2, "more. You make me want to", verb5, "and I will", verb6, "you forever. Nobody else could", verb7, "me, like you do.", adverb3, "yours.")

def start():
    print ("Pick a story")
    print()
    print ("Funny vacation story: press 1")
    print ("Worst bedtime story: press 2")
    print ("Love story: press 3 ")
    story = input('story: ')
    if story == '1': 
        madlibs()
    elif story == '2':    
        madlibs2()
    elif story=='3':
        madlibs3()    
    else:
        exit()

win_condition = ["Try again!", "You won!"]
options = {"scissors":"rock","paper":"scissors","rock":"paper"}
score = 0
def game():
    global score

    valid = False
    while valid is False:
        do = input("Rock, paper or scissors: ")
        valid = do in options

    cpu = random.choice(list(options))
    same = cpu == do
    won = options[cpu] == do
    score += int(won)

    if same:
        print("You both chose: " + do + "!")
    else:
        print("You chose: " + do + "!")
        print("Your opponent chose: " + cpu + "!")

    print(win_condition[int(won)])
    print("- "*10)
    print("Your score: " + str(score))
    print("- "*10)
    game()

print("Do you wnat to play a game? (yes/no)")
print()
answer = input()
if answer.lower() == "yes":
    print("Choose 1 - Magic 8, 2 -  Random #, 3, 4!")
    choice = input()
    if choice == "1":
        print('  __  __          _____ _____ _____    ___  ')
        print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
        print(' | \  / |  /  \ | |  __  | || |      | (_) |')
        print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
        print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
        print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
        print('')
        print('')
        print('')
        print('Hello World, I am the Magic 8 Ball, What is your name?')
        print()
        name = input()
        print('hello ' + name)

        Magic8Ball()
    elif choice == "2":
        print("")
        Jokes()
    elif choice == "3":
        start()
    elif choice == "4":
        game()
    else:
        print("Enter vaild number")
elif answer.lower() == "no":
    print("Okay")
else:
    print("Please enter yes or no.")