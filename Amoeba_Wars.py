dim = int(input("Enter the dimension of the square "))

def making_grid(dimension):
    gridline = []
    for i in range(dimension):
        gridline.append(" ")
    grid = []
    for i in range(dimension):
        grid.append(list(gridline))
    grid[-1][0] = 'O'
    grid[0][-1] = 'X'
    return grid

grid = making_grid(dim)

def get_scores(grid_map):
    X_score = sum('X' in s for nested in grid_map for s in nested)
    O_score = sum('O' in s for nested in grid_map for s in nested)
    return O_score, X_score

def print_centered_scores(O_score, X_score):
    scores = f"O {O_score} - {X_score} X"
    cntrd_scores = scores.center(20)
    print(cntrd_scores)
    
def print_grid(dimension,grid_map):
    O_score, X_score = get_scores(grid_map)
    print_centered_scores(O_score, X_score)
    temp_dim = dimension
    while temp_dim:
        print(temp_dim, end = " |")
        for elem in grid_map[-temp_dim]:
            print(elem, end = "|")
        print("\n")
        temp_dim -= 1
    print(" ", end = " |")
    for char_ord in range(65,65+dimension):
        print(chr(char_ord), end = "|")
    print("\n")
    
print_grid(dim,grid)

row_vals_usr_to_pc = {}
row_vals_pc_to_usr = {}
temp_dim = dim
for row in range(dim):
    row_vals_usr_to_pc[temp_dim] = row
    row_vals_pc_to_usr[row] = temp_dim
    temp_dim = temp_dim - 1
    
col_vals_usr_to_pc = {}
col_vals_pc_to_usr = {}
for col in range(dim):
    col_vals_usr_to_pc[chr(65+col)] = col
    col_vals_pc_to_usr[col] = chr(65+col)
    
def mvs_fr_plyr(grid_map,plyr):
    dim = len(grid_map)
    moves = []
    if plyr=='X':
        opp_plyr = "O"
    else:
        opp_plyr = "X"
        
    for row in range(len(grid_map)):
        for col in range(len(grid_map[row])):
            if grid_map[row][col] == plyr:
                
                if ((row-1) >= 0 and (col-1) >= 0) and (grid_map[row-1][col-1] == " " or grid_map[row-1][col-1] == opp_plyr):
                    moves.append((row_vals_pc_to_usr[row-1],col_vals_pc_to_usr[col-1]))
                    
                if ((col-1) >= 0) and (grid_map[row][col-1]==" " or grid_map[row][col-1] == opp_plyr):
                    moves.append((row_vals_pc_to_usr[row],col_vals_pc_to_usr[col-1]))
                    
                if ((row+1) < dim and (col-1) >= 0) and (grid_map[row+1][col-1] == " " or grid_map[row+1][col-1] == opp_plyr):
                    moves.append((row_vals_pc_to_usr[row+1],col_vals_pc_to_usr[col-1]))
                    
                if ((row-1) >= 0 and (col+1) < dim) and (grid_map[row-1][col+1] == " " or grid_map[row-1][col+1] == opp_plyr):
                    moves.append((row_vals_pc_to_usr[row-1],col_vals_pc_to_usr[col+1]))
                    
                if ((col+1) < dim) and (grid_map[row][col+1]==" " or grid_map[row][col+1]== opp_plyr):
                    moves.append((row_vals_pc_to_usr[row],col_vals_pc_to_usr[col+1]))
                    
                if ((row+1) < dim and (col+1) < dim) and (grid_map[row+1][col+1] == " " or grid_map[row+1][col+1] == opp_plyr):
                    moves.append((row_vals_pc_to_usr[row+1],col_vals_pc_to_usr[col+1]))
                    
                if ((row+1) < dim) and (grid_map[row+1][col] == " " or grid_map[row+1][col] == opp_plyr):
                    moves.append((row_vals_pc_to_usr[row+1],col_vals_pc_to_usr[col]))
                    
                if ((row-1) >= 0) and (grid_map[row-1][col] == " " or grid_map[row-1][col] == opp_plyr):
                    moves.append((row_vals_pc_to_usr[row-1],col_vals_pc_to_usr[col]))
    
    return list(set(moves)) if moves else []

# O plyr 1st move
moves_for_player = mvs_fr_plyr(grid, 'O')

if moves_for_player:
    print("Moves that can be made ", end="")
    for move in moves_for_player:
        print(move, end = " ")
    print("\n")
else:
    print("end game")
    
def check_if_valid_move(move, valid_moves):
    if move in valid_moves:
        return True
    return False

def aftr_moves(grid_map,move,plyr):
    if grid_map[row_vals_usr_to_pc[move[0]]][col_vals_usr_to_pc[move[1]]] == " ":
        grid_map[row_vals_usr_to_pc[move[0]]][col_vals_usr_to_pc[move[1]]] = plyr
    else:
        grid_map[row_vals_usr_to_pc[move[0]]][col_vals_usr_to_pc[move[1]]] = "#"
    return grid_map

while True:
    first_O_move = input("Enter Move According To The Above Values ")
    first_O_move = (int(first_O_move.replace(" ","").split(",")[0]), first_O_move.replace(" ","").split(",")[1])
    if check_if_valid_move(first_O_move, moves_for_player):
        break
    print("Enter the right value")
    
grid = aftr_moves(grid,first_O_move,'O')

print_grid(dim,grid)

curr_player = "X"
Flag = True

while Flag:
    for _ in range(3):
        print_grid(dim, grid)
        moves_for_player = mvs_fr_plyr(grid,curr_player)
        if moves_for_player:
            print(f"Moves that can be made by player {curr_player} ", end="=> ")
            for move in moves_for_player:
                print(move, end = " ")
        else:
            Flag = False
            break
        print("\n")
        while True:
            move = input("Enter Move According To The Above Values ")
            move = (int(move.replace(" ","").split(",")[0]), move.replace(" ","").split(",")[1])
            if check_if_valid_move(move, moves_for_player):
                break
            print("Enter the right value")
        grid = aftr_moves(grid,move,curr_player)
    if curr_player == "X":
        curr_player = "O"
    else:
        curr_player = "X"
        
final_X_score, final_O_score = get_scores(grid)

if final_X_score>final_O_score:
    print('Player-X wins')
elif final_X_score<final_O_score:
    print('Player-O wins')
else:
    print('Tie')
