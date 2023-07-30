import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Piedra, Papel o Tijera: ')

    if not user_option.lower() in options:
        print('Esa opción no es válida')
        return None, None
        # continue

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option

def checkRules(user_option, computer_option, points_user, points_computer):
    if user_option.upper() == computer_option.upper():
        print('Empate!')
    elif user_option.upper() == 'Piedra'.upper():
        if computer_option.upper() == 'Tijera'.upper():
            print('Piedra gana a Tijera')
            print('User gana')
            points_user += 1
        else:
            print('Papel gana a Piedra')
            print('Computer gana')
            points_computer += 1
    elif user_option.upper() == 'Papel'.upper():
        if computer_option.upper() == 'Piedra'.upper():
            print('Papel gana a Piedra')
            print('User gana')
            points_user += 1
        else:
            print('Tijera gana a Papel')
            print('Computer gana')
            points_computer += 1
    elif user_option.upper() == 'Tijera'.upper():
        if computer_option.upper() == 'Papel'.upper():
            print('Tijera gana a Papel')
            print('User gana')
            points_user += 1
        else:
            print('Piedra gana a Tijera')
            print('Computer gana')
            points_computer += 1
    return points_user, points_computer

def check_wins(points_user, points_computer):
    if points_user > points_computer:
        print("USER WINS")
    else:
        print("COMPUTER WINS")

def run_game():
    points_user = 0
    points_computer = 0
    rounds = 1
    while True:
        print('*', 15)
        print('ROUND', rounds)
        print('*' * 15)
        rounds += 1
        
        user_option, computer_option = choose_options()
        
        if( user_option == None and computer_option == None):
            continue
        
        points_user, points_computer = checkRules(user_option, computer_option, points_user, points_computer)
                
        print('*' * 5, 'User Points:', points_user, '*' * 5, 'Computer Points:', points_computer)
        
        if points_computer > 2 or points_user > 2:
            check_wins(points_user, points_computer)
            break
        
run_game()