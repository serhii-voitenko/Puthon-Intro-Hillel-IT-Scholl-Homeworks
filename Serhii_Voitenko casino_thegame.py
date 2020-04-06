import random
from datetime import datetime
import json

wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
wheel2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
wheel3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
choice1 = random.choice(wheel1)
choice2 = random.choice(wheel2)
choice3 = random.choice(wheel3)
result_table = [choice1, choice2, choice3]
user_info = {}
total_cash = 0


def game():
    user_data()
    user_interaction()
    play(result_table)
    now = datetime.now()
    user_info.update({'Date_of_playing: ': now.strftime("%Y-%m-%d %H:%M")})
    with open('Serhii_Voitenko Classwork casino_the_game.json', 'w') as json_file:
        json.dump(user_info, json_file, indent=4, sort_keys=True)


def user_data():
    global name, cash, age
    name = input('Hi, gamer! What is your name? ')
    age = int(input('How old are you? '))
    cash = float(input('How much money do you have? '))
    try:
        age = int(age)
        cash = float(cash)
    except ValueError:
        print(' Incorrect value. Please restart the program. ')
    while cash == 0:
        cash = float(input('You should have enough money! Come across! '))
    user_info.update({'Name: ': name, 'Age: ': age, 'Had_money: ': cash})
    return user_info


def user_interaction():
    print('Do you want to start the game? ')
    user_decision = str(input('Enter \'Yes\' or \'No\': '))
    if user_decision == 'Yes':
        print(f' You got:  {result_table}')
        return result_table
    else:
        while user_decision == 'No':
            user_decision = str(input('You can\'t go away!! \nLook!!! \nYou will WIN! I know it!!! \n'
                                      'Enter something to continue.. '))
            return user_interaction()
        while user_decision != 'No':
            user_decision = str(input('I don\'t know what we are doing.... Please try again... '))
            return user_interaction()


def play(result_table):
    global total_cash
    if result_table.count('A') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 9
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('A') == 3:
        total_cash = cash + 90
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('A') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 18
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('B') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 8
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('B') == 3:
        total_cash = cash + 80
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('B') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 16
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('C') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 7
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('C') == 3:
        total_cash = cash + 70
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('C') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 14
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('D') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 6
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('D') == 3:
        total_cash = cash + 60
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('D') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 12
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('E') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 5
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('E') == 3:
        total_cash = cash + 50
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('E') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 10
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('F') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 4
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('F') == 3:
        total_cash = cash + 40
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('F') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 8
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('G') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 3
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('G') == 3:
        total_cash = cash + 30
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('G') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 6
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('H') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 2
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('H') == 3:
        total_cash = cash + 20
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('H') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 4
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('I') == 2 and result_table.count('XXX') != 1:
        total_cash = cash + 1
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('I') == 3:
        total_cash = cash + 10
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('I') == 2 and result_table.count('XXX') == 1:
        total_cash = cash + 2
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('XXX') == 2:
        total_cash = cash + 10
        user_info.update({'Cash_after_game:': total_cash})
    elif result_table.count('XXX') == 3:
        total_cash = cash + 100
        user_info.update({'Cash_after_game:': total_cash})
    else:
        while total_cash == cash:
            print('You didn\'t win right now.. But you didn\'t lose!!! Try again!')
            return result_table
    print(f'I told you!!! YOU WIN!!! Now you have: {total_cash}')
    return user_info


game()
