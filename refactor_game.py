#Vamos a refactorizar el código del juego del curso de fundamentos de python

import random

options= ('piedra', 'papel', 'tijera')
user_wins = 0
computer_wins = 0
def choose_options():
   option = input("Piedra, papel o tijera => ")
   option = option.lower()
   if option not in options:
    print("Esa opción no es válida")
    return None, None
   else:
    option_computer = random.choice(options)
    print("User option =>", option)
    print("Computer option =>", option_computer)
    return option, option_computer
   
def check_rules(option, option_computer, computer_wins, user_wins):
    if option == option_computer:
        print("Empate!")
    elif option == 'piedra':
     if option_computer == 'tijera':
       print("Piedra gana a tijera")
       print("Ganaste!")
       user_wins += 1
     else: 
       print("Papel gana a piedra")
       print("Perdiste!")
       computer_wins += 1
    elif option == 'papel':
     if option_computer == 'piedra':
       print("papel gana a piedra")
       print("Ganaste!")
       user_wins += 1
     else:
       print("Tijera gana a papel")
       print("Perdiste")
       computer_wins += 1
    elif option == 'tijera':
     if option_computer == 'papel':
       print("Tijera gana a papel")
       print("Ganaste!")
       user_wins += 1
     else: 
       print("Piedra gana a tijera")
       print("Perdiste!")
       computer_wins += 1
    return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if computer_wins == 2:
    return "La computadora ha ganado "

  if user_wins == 2:
    return "Has sido el ganador"
    
  
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print( '*' *10)
        print("Round", rounds)
        print( '*' *10)
        print("Computer wins =>", computer_wins)
        print("User wins =>", user_wins)
        rounds += 1
        option, option_computer = choose_options()
        user_wins, computer_wins = check_rules(option, option_computer,computer_wins, user_wins)
        result = check_winner(user_wins, computer_wins)
        if result != None:
            print(result)
            break
        
run_game()