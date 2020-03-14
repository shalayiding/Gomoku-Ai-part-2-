# Gomoku-AI (PART 2)
basic Gomoku AI using minimax
You can find the Mnimax algorithm here (https://www.youtube.com/watch?v=l-hh51ncgDI)
the basic game can be found in link(https://github.com/shalayiding/Gomoku-Game)

## How to
    1.install python 2.x or 3.x(recommended)
    2.Install pygame
    $pip install pygame
    3.Clone the repository:
    $git clone https://github.com/shalayiding/Gomoku-Ai-part-2-
    4.run Gomuku_test.py
    $python Gomuku_test.py
## Minimax()
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

## BoardMatrix()
```
    1 - > white stone, 2 -> black stone
        [[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  
```    
##  Screen shot
![Gomoku](https://raw.githubusercontent.com/shalayiding/Gomoku-Game/master/screenshot1.PNG)

