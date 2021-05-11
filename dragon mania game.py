import random


def start():
    mode = input('choose mode Easy,Normal or Hard - ')
    mode = mode.lower()
    if mode == 'easy':
        easy()
    elif mode == 'normal':
        normal()
    elif mode == 'hard':
        hard()
    else:
        print('You are not allowed to enter the game. Please write the input given')
        start()


def easy():
    print('Dragon is sleeping')
    choose = input('You want to escape or fight with dragon - ')
    choose.lower()
    if choose == 'escape':
        stop()
    elif choose == 'fight':
        result = random.randint(0, 100)
        if result < 50:
            print("You Loose the Game")
            stop()
        else:
            diamonds = result-50
            print(f'you get {diamonds} diamonds.')
            if diamonds > 10:
                hard()
            else:
                print("you won the game")
                stop()
    else:
        print("wrong input")
        start()


def normal():
    print("Welcome to normal Level")
    print('Dragon is going to take sleep')
    print("Get ready to fight !")
    result = random.randint(0, 500)
    if result < 300:
        print("You Loose the Game")
        stop()
    else:
        diamonds = result-300
        print(f'you get {diamonds} diamonds.')
        if diamonds > 100:
            hard()
        else:
            print("you won the game")
            stop()


def hard():
    print("Welcome to Hard Level")
    print('Get ready for fight with dragon !')
    result = random.randint(0, 1000)
    if result < 850:
        print("You Loose the Game")
        stop()
    else:
        print("Get ready for fight with king of dragons")
        second_battle = random.randint(-1, 1)
        if second_battle == 1:
            print('You won battle with King but didn\'t got diamonds')
            diamonds = result - 850
            print(f'you get {diamonds} diamonds.')
            if diamonds > 200:
                hard()
            else:
                print("you won the game")
                stop()
        else:
            stop()


def stop():
    again = input("do you want to play the game again (enter yes to play again, no to leave the game) - ")
    again = again.lower()
    if again == 'yes':
        start()
    elif again == 'no':
        print('Bye! come soon!')
    else:
        print("Wrong Input ! you are out of the game")
        stop()


start()
