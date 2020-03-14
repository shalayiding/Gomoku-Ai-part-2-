import numpy as np 
from random import seed
from random import randint
from player import Check_pos_inrange
#create random move from the left location 
def Create_random_move(available_location):
    print(len(available_location))

#give player type like black for white to check if any winner condition is satisfy
def Check_all_for_type(board_status,player_type,h,w,size_h,size_w):
    check_horizontal=[]
    check_vertical = []
    check_left_to_right = []
    check_right_to_left=[]
    link_len = 3
    if board_status[h][w] == player_type:
        #check horizontal 
        pos_w = w
        while pos_w < size_h and board_status[h][pos_w]==player_type:
            pos_w+=1
            check_horizontal.append([h,pos_w])
        #check vertical 
        pos_h = h
        while pos_h < size_h and board_status[pos_h][w]==player_type:
            pos_h+=1
            check_vertical.append([pos_h,w])
        #check left top to right down
        pos_w,pos_h = w,h
        while pos_w < size_w and pos_h < size_h and board_status[pos_h][pos_w]==player_type:
            pos_w+=1
            pos_h+=1
            check_left_to_right.append([pos_h,pos_w])
        #check right down to left top
        pos_w,pos_h = w,h
        while pos_w >= 0 and pos_h < size_h and board_status[pos_h][pos_w]==player_type:
            pos_w-=1
            pos_h+=1
            check_right_to_left.append([pos_h,pos_w])
        
        if len(check_left_to_right) >=link_len or len(check_right_to_left) >=link_len or  len(check_horizontal)>=link_len or len(check_vertical)>=link_len:
            return player_type

        check_horizontal=list()
        check_left_to_right=list()
        check_right_to_left=list()
        check_vertical=list()
    return 0   


#check_the_winner will take board_status matrix
#return 0,1,2 value respectively as 0 for not done 
# 1 for white win 2 for black win 3 for tie 
def Check_the_winner(board_status):
    white_win = 0
    black_win = 0
    tie = 3
    # board information 1 is white 2 is black 0 is empty
    for h in range(0,len(board_status)):
        for w in range(0,len(board_status[h])):
            if white_win == 0 and black_win==0:
                white_win = Check_all_for_type(board_status,1,h,w,len(board_status),len(board_status[h]))
                black_win = Check_all_for_type(board_status,2,h,w,len(board_status),len(board_status[h]))
            if board_status[h][w]==0:
                tie = 0
    return white_win,black_win,tie


def minimax(board_status,depth,findmax,alpha,beta):
    white_result,black_result,tie = Check_the_winner(board_status)
    if white_result!=0 or black_result!=0 or tie !=0:
        if white_result!=0:
            return -1
        elif black_result!=0:
            return 1
        else:
            return 0
    if findmax:
        best_reward = -99999
        for h in range(0,len(board_status)):
            for w in range(0,len(board_status[h])):
                if board_status[h][w] == 0:
                    board_status[h][w]=2
                    reward = minimax(board_status,depth+1,False,alpha,beta)
                    board_status[h][w]=0
                    best_reward=max(reward,best_reward)
                    alpha = max(best_reward,reward)
                    if beta <=alpha:
                        break 
        return best_reward
    else:
        best_reward = +99999
        for h in range(0,len(board_status)):
            for w in range(0,len(board_status[h])):
                if board_status[h][w] == 0:
                    board_status[h][w]=1
                    reward = minimax(board_status,depth+1,True,alpha,beta)
                    board_status[h][w]=0
                    best_reward=min(reward,best_reward)
                    beta = min(reward,beta)
                    if beta <=alpha:
                        break 
        return best_reward




def Ai_move(white_current,black_current,all_location,board_status):
    bestreward = -99999
    pos = 0,0
    tmp_board = board_status
    for h in range(0,len(tmp_board)):
        for w in range(0,len(tmp_board[h])):
            if tmp_board[h][w] == 0:
                tmp_board[h][w]=2
                reward = minimax(tmp_board,0,False,-99999,99999)
                tmp_board[h][w]=0
                if reward > bestreward:
                    bestreward=reward
                    pos = h,w
        # Ai_move = randint(0,len(all_location)-1)
    pos = (pos[1]*40+17),(pos[0]*40)+8
    return pos





# board_test =       [[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]     

# print(Check_the_winner(board_test))











    