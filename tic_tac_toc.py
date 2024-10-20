# Program for playing rock paper scissor with your friends
from copy import deepcopy                               # for creating duplicate canvas

# Making a canvas with dot as a place holder in absence of 'x' or 'o'
canvas = [ [ '.', '.', '.' ], [ '.', '.', '.' ], [ '.', '.', '.' ] ]

def print_canvas(l = []):
    for a in l: print(a)

# Print the rules for playing
def list_rules() -> None:
    print_canvas(canvas)
    print("Canvas will be like the above only give the location where you want to set(Eg: 2 3)")
    print("You can't set on previously setted value")
    print("Player1 has 'x' as denotion in game canvas and Player2 will have 'o' as his denotion on canvas")


def check_if_won(l = []) -> bool:
    marks = [ 'x', 'o' ]
    # for checking if any row has been completed by only one player
    condition1 = any(( l[0][0]==l[0][1] and l[0][1]==l[0][2] and l[0][2] in marks, l[1][0]==l[1][1] and l[1][1]==l[1][2] and l[1][2] in marks, l[2][0]==l[2][1] and l[2][1]==l[2][2] and l[2][2] in marks))
    # for checking if any column has been completed by only one player
    condition2 = any(( l[0][0]==l[1][0] and l[1][0]==l[2][0] and l[2][0] in marks, l[0][1]==l[1][1] and l[1][1]==l[2][1] and l[2][1] in marks, l[0][2]==l[1][2] and l[1][2]==l[2][2] and l[2][2] in marks ))
    # for checking if any diagonal is been completed by only one player
    condition3 = any(( l[0][0]==l[1][1] and l[1][1]==l[2][2] and l[2][2] in marks, l[0][2]==l[1][1] and l[1][1]==l[2][0] and l[2][0] in marks ))
    if any((condition1,condition2,condition3)): return True
    return False

if __name__ == "__main__":
    c = 'y'
    while c.lower()=='y':
        list_rules()
        game_canvas = deepcopy(canvas)
        while True:
            try:
                print_canvas(game_canvas)
                player1 = list(map(int, input("Player1 chance : ").split()))
                if game_canvas[player1[0]-1][player1[1]-1] == '.': game_canvas[player1[0]-1][player1[1]-1] = 'x'
                if check_if_won(game_canvas): 
                    print("Player1 Won")
                    break
                print_canvas(game_canvas)
                player2 = list(map(int, input("Player2 chance : ").split()))
                if game_canvas[player2[0]-1][player2[1]-1] == '.': game_canvas[player2[0]-1][player2[1]-1] = 'o'
                if check_if_won(game_canvas): 
                    print("Player2 Won")
                    break
            except Exception as e:
                print(e)
                c = 'n'
                break
            
        c = input("Do you want to continue a new game?(Y/N) : ")
    else: print("See you soon!")