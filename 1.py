
from random import randint

def calc_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)
def game_ends(winner_name):
    print(f'{winner_name} won the game!')
game_running = True
game_results = []

while game_running == True:
    counter = 0
    new_round = True
    player = { 'name':'Manual', 'attack':13, 'heal':16, 'health':100}
    monster = { 'name':'raven', 'attack_min':10, 'attack_max':20, 'health':100}
    print('----'*7)
    print('Enter player name:')
    player['name'] = input()
    print('----'*7)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_round == True:

        counter += 1
        player_won = False
        monster_won = False    
        print('----'*7)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit game')
        print('4) Show results')
        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calc_monster_attack(monster['attack_min'], monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True

            print('Attack')
        elif player_choice == '2':
            player['health'] += player['heal']
            print( player['name'] +' health incresed to ' + str(player['health']) )
            print('Player attacked by monster')
            player['health'] = player['health'] - calc_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True

        elif  player_choice == '3':
            print('Player exits from the game')
            new_round = False
            game_running = False

        elif player_choice == '4':
            for result in game_results:
                print(result)

        else:
            print('Invalid input')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' health left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health left')
        elif player_won:
            game_ends(player['name'])
            player_round_result = {'name':player['name'], 'health': player['health'], 'rounds':counter, 'won':'Player'}
            monster_round_result = {'name':monster['name'], 'health': monster['health'], 'rounds':counter, 'lose':'Monster'}
            game_results.append(player_round_result)
            game_results.append(monster_round_result)
            print(player_round_result)
            print(monster_round_result)
            new_round = False
        elif monster_won:
            game_ends(monster['name'])
            player_round_result = {'name':player['name'], 'health': player['health'], 'rounds':counter, 'lose':'Player'}
            monster_round_result = {'name':monster['name'], 'health': monster['health'], 'rounds':counter, 'won':'Monster'}
            game_results.append(player_round_result)
            game_results.append(monster_round_result)
            print(player_round_result)
            print(monster_round_result)
            new_round = False

       

