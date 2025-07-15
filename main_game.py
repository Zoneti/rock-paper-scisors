import random
import os

move_list = ['papel', 'pedra', 'tesoura', 'lagarto', 'spock']
move_check = [0, 1, 2, 3, 4]
player_count = 0
computer_count = 0
game_exit = 0

print('=========================================')
print("Bem-vindo ao jogo Pedra, Papel, Tesoura, Lagarto e Spock!")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_print():
    print('=========================================')
    print('Digite "r" para ver as regras do jogo ou qualquer outra tecla para continuar.')
    choice = input().lower()
    if choice == 'r':
        print_rules()
    print('\nPLACAR:')
    print(f'Você: {player_count}')
    print(f'Computador: {computer_count}')
    print('\n')
    print('Escolha seu lance:')
    print('0 - Papel | 1 - Pedra | 2 - Tesoura | 3 - Lagarto | 4 - Spock')

def print_rules():
    print('=========================================')
    print('Regras do jogo:')
    print('Tesoura corta Papel')
    print('Papel cobre Pedra')
    print('Pedra esmaga Lagarto')
    print('Lagarto envenena Spock')
    print('Spock desintegra Tesoura')
    print('Tesoura decapita Lagarto')
    print('Lagarto come Papel')
    print('Papel refuta Spock')
    print('Spock vaporiza Pedra')
    print('Pedra quebra Tesoura')
    print('=========================================')
    print('Digite qualquer tecla para continuar...')
    _ = input()
    clear_console()


def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in move_check:
                raise
            return move_list[player_move]
        except Exception as e:
            print('Opção inválida! Digite um número entre 0 e 4')

def select_winner(p_move, c_move):
    global player_count, computer_count

    #validacao papel
    if p_move == 'papel':
        if c_move == 'pedra':
            player_count += 1
            return 'p'
        elif c_move == 'spock':
            player_count += 1
            return 'p'
        elif c_move == 'tesoura':
            computer_count += 1
            return 'c'
        elif c_move == 'lagarto':
            computer_count += 1
            return 'c'
        else:
            return 'd'
    #validacao pedra
    elif p_move == 'pedra':
        if c_move == 'tesoura':
            player_count += 1
            return 'p'
        elif c_move == 'lagarto':
            player_count += 1
            return 'p'
        elif c_move == 'papel':
            computer_count += 1
            return 'c'
        elif c_move == 'spock':
            computer_count += 1
            return 'c'
        else:
            return 'd'
    #validacao tesoura
    elif p_move == 'tesoura':
        if c_move == 'papel':
            player_count += 1
            return 'p'
        elif c_move == 'lagarto':
            player_count += 1
            return 'p'
        elif c_move == 'pedra':
            computer_count += 1
            return 'c'
        elif c_move == 'spock':
            computer_count += 1
            return 'c'
        else:
            return 'd'
    #validacao lagarto
    elif p_move == 'lagarto':
        if c_move == 'spock':
            player_count += 1
            return 'p'
        elif c_move == 'papel':
            player_count += 1
            return 'p'
        elif c_move == 'pedra':
            computer_count += 1
            return 'c'
        elif c_move == 'tesoura':
            computer_count += 1
            return 'c'
        else:
            return 'd'
    #validacao spock
    elif p_move == 'spock':
        if c_move == 'tesoura':
            player_count += 1
            return 'p'
        elif c_move == 'pedra':
            player_count += 1
            return 'p'
        elif c_move == 'papel':
            computer_count += 1
            return 'c'
        elif c_move == 'lagarto':
            computer_count += 1
            return 'c'
        else:
            return 'd'
        
while game_exit == 0:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)

    print('')
    print('=========================================')
    print(f'Sua jogada: {player_move.upper()}')
    print(f'Jogada do Computador: {computer_move.upper()}')

    if winner == 'p':
        print('Você venceu!')
    elif winner == 'c':
        print('Você perdeu!')
    else:
        print('Empate!')
    print('=========================================')
    while True:
        print('Jogar Novamente? 0 - Sim | 1 - Não')
        try:
            again = int(input())
            if again not in [0, 1]:
                raise
            game_exit = again
            break
        except Exception as e:
            print('Opção inválida! Digite 0 ou 1')
    
    clear_console()