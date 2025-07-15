import random
import os

move_list = ['papel', 'pedra', 'tesoura']
player_count = 0
computer_count = 0
game_exit = 0

print('=========================================')
print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")

def main_print():
    print('=========================================')
    print('\nPLACAR:')
    print(f'Você: {player_count}')
    print(f'Computador: {computer_count}')
    print('\n')
    print('Escolha seu lance:')
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')

def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return move_list[player_move]
        except Exception as e:
            print(e)

def select_winner(p_move, c_move):
    global player_count, computer_count

    #validacao papel
    if p_move == 'papel':
        if c_move == 'pedra':
            player_count += 1
            return 'p'
        elif c_move == 'tesoura':
            computer_count += 1
            return 'c'
        else:
            return 'd'
    #validacao pedra
    elif p_move == 'pedra':
        if c_move == 'tesoura':
            player_count += 1
            return 'p'
        elif c_move == 'papel':
            computer_count += 1
            return 'c'
        else:
            return 'd'
    #validacao tesoura
    elif p_move == 'tesoura':
        if c_move == 'papel':
            player_count += 1
            return 'p'
        elif c_move == 'pedra':
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
    
    os.system('cls' if os.name == 'nt' else 'clear')