def is_taken(num: int, board: str) -> bool:
    return str(num) not in board

def check_for_win(wins: list, board: str) -> bool:
    # Flatten the board into a single string without '|' and '\n'
    clean_board = board.replace('|', '').replace('\n', '')

    # Check each winning combination
    for win in wins:
        if (clean_board[win[0] - 1] == 'X' and clean_board[win[1] - 1] == 'X' and clean_board[win[2] - 1] == 'X') or (clean_board[win[0] - 1] == 'O' and clean_board[win[1] - 1] == 'O' and clean_board[win[0]- 1] == 'O'):
            return True
    return False

def get_user_input(player: int, board: str) -> str:
    print(board)
    print()
    print(f"Player {player}'s turn:")
    
    # Check to see if we have a digit or not.
    user_number_str: str = input(f'Player {player}, select an available square between 1 and 9: ')
    while not user_number_str.isdigit():
        print('Please enter a valid integer.')
        user_number_str = input(f'Player {player}, select an available square between 1 and 9: ')

    # Check to see if input is between 1 and 9.
    user_number_int: int = int(user_number_str)
    while user_number_int > 9 or user_number_int < 1:
        print('Please ensure your number is between 1 and 9.')
        user_number_str = input(f'Player {player}, select an available square between 1 and 9: ')
        user_number_int = int(user_number_str)

    # Checks to see if the square is already taken.
    while is_taken(user_number_int, board):
        print('Please ensure your square is not taken.')
        user_number_str = input(f'Player {player}, select an available square between 1 and 9: ')
        user_number_int = int(user_number_str)

    # Replace the number with the player's mark.
    if player == 1:
        board = board.replace(str(user_number_int), 'X')
    else:
        board = board.replace(str(user_number_int), 'O')
    
    return board

def main():
    wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    player = 1
    over: bool = False
    board: str = '|1|2|3|\n|4|5|6|\n|7|8|9|'

    while not over:
        
        board = get_user_input(player, board)

        if(check_for_win(wins, board) == True):
            if(player == 1):
                print(board)
                print('Game over. Player 1 wins!')
                break
            else:
                print(board)
                print('Game over. Player 2 wins!')
                break

        else:
            if player == 1:
                player = 2
            else:
                player = 1

if __name__ == '__main__':
    main()