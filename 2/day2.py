import re
#only 12 red cubes, 13 green cubes, and 14 blue cubes
def import_values(path):
    input_file = open(path, 'r', encoding='utf-8')
    return input_file

p_red = 12
p_green = 13
p_blue = 14

def parse_input():
    values = import_values("./2/input")
    for x in values:
        # get Game IDs
        game = []
        nr = re.search(r'Game (\d+)', x)
        game_nr = nr.group(1)
        game.append(game_nr)
        #Get Draws
        value_list = x.split(';')
        print(game)





#    for game in values:
#        possible = 0
#        game_list = game.split(':')
#        game_nr_lst = str(game_list[0]).split(' ')
#        game_nr = game_nr_lst[1]
#        game_list.pop(0)
#        #print(game_list)
#        game_results = game_list[0].split(";")
#        for draws in game_results:
#              #print(draws)
#              single_draw = draws.split(',')
#              print(single_draw)
              
        #if possible == 1:
            #print("game is possible") 
        #else:
            #print("game is not possible")
        #print(game_nr)
parse_input()