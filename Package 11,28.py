import time

#initialising the tic-tac-toe board
board = { 1 : ' ', 2 : ' ', 3 : ' ',
          4 : ' ', 5 : ' ', 6 : ' ', 
          7 : ' ', 8 : ' ', 9 : ' '}

#initialising the variables
count = 0		#track number of filled slots
winner = False		#if anyone wins
play = True		#if the game should continue
tie = False		#if there is a tie
curr_player = ''	#store current player identifier
player_details = []	#store player identifier and marker

#get identifier and marker from player
def get_player_details(curr_player):
    if curr_player == 'A':
        return ['B','O']
    else:
        return ['A','X']
    
#print the tic-tac-toe board
def print_board():
    for i in board:
        print( i, ':', board[i], ' ', end='')
        if i%3 == 0:
            print()

#winning possibility combinations
def win_game(marker, player_id):
    if board[1] == marker and board[2] == marker and board[3] == marker or \
       board[4] == marker and board[5] == marker and board[6] == marker or \
       board[7] == marker and board[8] == marker and board[9] == marker or \
       board[1] == marker and board[4] == marker and board[7] == marker or \
       board[2] == marker and board[5] == marker and board[8] == marker or \
       board[3] == marker and board[6] == marker and board[9] == marker or \
       board[1] == marker and board[5] == marker and board[9] == marker or \
       board[3] == marker and board[5] == marker and board[7] == marker:

        print_board()
        time.sleep(1)
        print("\nPlayer", player_id, "wins!")
        return True
    else:
        return False

#input from player
def insert_input(slot_num, marker):
    while board[slot_num] != ' ':
        print("\nSpot taken, pick another number!")
        slot_num = int(input())
    board[slot_num] = marker

#if player wants to play again
def play_again():
    print("\nDo you want to play again?")
    play_again = input()

    if play_again.upper() == 'Y':
        for z in board:
            board[z] = ' '
        return True
    else:
        print("\nThanks for playing!")
        return False
    
#mian program
while play:

    print_board()

    player_details = get_player_details(curr_player)
    curr_player = player_details[0]
    print("\nPlayer {}: Enter a number between 1 and 9".format(curr_player))
    input_slot = int(input())

    #inserting 'X' or 'O' in a spot
    insert_input(input_slot, player_details[1])
    count += 1
    
    #if a player has won
    winner = win_game(player_details[1], curr_player)
    if count == 9 and not winner:
        print("\nIt's a tie!!")
        tie = True
        print_board()

    #if players want to play again
    if winner or tie:
        play = play_again()
        if play:
            curr_player = ''
            count = 0
