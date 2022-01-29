'''
Game not finished  : when neither side has three in a row but the grid still has empty cells.
Draw : when no side has a three in a row and the grid has no empty cells.
X wins : when the grid has three X’s in a row.
O wins : when the grid has three O’s in a row.
Impossible : when the grid has three X’s in a row as well as three O’s in a row, 
or there are a lot more X's than O's or vice versa
 (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).
'''
# write your code here
a = input("Enter cells:")
print("---------")
print("|", a[0], a[1], a[2], "|")
print("|", a[3], a[4], a[5], "|")
print("|", a[6], a[7], a[8], "|")
print("---------")


def count_empty(str):
    count = 0
    for x in range(0, len(str)):
        if str[x] == ' ' or str[x] == '_':
            count += 1
    return count

mates = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
         [0, 3, 6], [1, 4, 7], [2, 5, 8],
         [0, 4, 8], [2, 4, 6]]
    
def check_victory(s):
    vic_list = []
    for mate in mates:
        if s[mate[0]] == s[mate[1]] == s[mate[2]]:
            vic_list.append(s[mate[0]])  # O or X
    if len(vic_list) == 1:
        return vic_list[0]
    if len(vic_list) == 2:
        return 'I' 
    return 'F' 
        
def check_finish():
    if check_victory(a) in ('O', 'X'):
        return True
    if count_empty(a) == 0:
        return True
    if count_empty(a) > 0:
        return False
    return False

def check_impossible(str):
    count_x = 0
    count_o = 0
    for x in range(0, len(str)):
        if str[x] == 'X':
            count_x += 1
        elif str[x] == 'O':
            count_o += 1
    if (max(count_x, count_o) - min(count_x, count_o)) > 1:
        return True
    if check_victory(a) == 'I':
        return True
    return False

if check_impossible(a) == True:
    print("Impossible")            
elif check_finish() == False:        
    print("Game not finished")
elif check_victory(a) == 'F' and count_empty(a) == 0:     
    print("Draw")
elif check_victory(a) == 'X':
    print("X wins")
elif check_victory(a) == 'O':
    print("O wins")
