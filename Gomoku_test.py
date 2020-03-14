import pygame 
from player import Check_pos_inrange
from player import check_who_win
import Gomoku_AI

#init the basic game function 
pygame.init()
width,height = 600,600
gameDisplay = pygame.display.set_mode([width,height])
pygame.display.set_caption('Gomoku')

#setting gomoku board image and scaling the image 
gomoku_board = pygame.image.load("Images/gomoku_board.gif").convert()
pygame.display.flip()
Gaming = True
gomoku_board = pygame.transform.scale(gomoku_board,(width,height))
gameDisplay.blit(gomoku_board, (0, 0))

#setting gomoku stones  
white_stone = pygame.image.load("Images/white_stone.png")
black_stone = pygame.image.load("Images/black_stone.png")

white_stone = pygame.transform.scale(white_stone,(20,20))
black_stone = pygame.transform.scale(black_stone,(20,20))

all_location = []
Ai_board_scaller = 5,5
for i in range(17,width//Ai_board_scaller[0],40):
    for j in range(8,height//Ai_board_scaller[1],40):
        tmp = [i,j]
        all_location.append(tmp)



white_current = [] #white first 
black_current = []
is_white = True
white_win = False
black_win = False
red = (255,0,0)
green = (0, 255, 0) 
#settig winner text 
font = pygame.font.SysFont('comicsansms', 30) 
white_win_text = font.render("White Win",True,red,green)
black_win_text = font.render("Black Win",True,red,green)
tie_text = font.render("Tie",True,red,green)
white_win_rect = white_win_text.get_rect()
black_win_rect = black_win_text.get_rect()
tie_rect = tie_text.get_rect()
white_win_rect.center = (width//2,height//2)
black_win_rect.center = (width//2,height//2)
tie_rect.center = (width//2,height//2)
#setting game record file and list 
Game_Record = []
record_f = open("Game_record.txt","a")
board_status_f = open("Board_status_matrix.txt","a")
RESET = False
Gomoku_AI.Create_random_move(all_location)
#board 
board_status = []
Game_tie =False

for j in range(8,height//Ai_board_scaller[0],40):
    tmp = []
    for i in range(17,width//Ai_board_scaller[1],40):    
        tmp.append(0)
    board_status.append(tmp)


while Gaming:
    # for data in test_data:
    #     gameDisplay.blit(black_stone,data)
    
    for event in pygame.event.get():
        # print(event)
        
        #update_board_status 
        
        white_win_status,black_win_status,tie = Gomoku_AI.Check_the_winner(board_status)
        # print(white_win_status,black_win_status,tie)
        if white_win_status == 1 or black_win_status == 2 :
            if white_win_status == 1:
                white_win=True
            elif black_win_status==2:
                black_win=True
            else:
                Game_tie=True

        if not is_white:
            pos = Gomoku_AI.Ai_move(white_current,black_current,all_location,board_status)    
            black_current.append(list(pos))
            is_white=True
            gameDisplay.blit(black_stone,pos)
            # black_win=check_who_win(black_current)
            Game_Record.append([0,pos])
            for data in Game_Record:
                tmp = data[1]
                matrix_w,matrix_h=tmp[0],tmp[1]
                matrix_w = matrix_w-17
                matrix_h = matrix_h-8
                if data[0]==0:
                    board_status[matrix_h//40][matrix_w//40] = 2
                else:
                    board_status[matrix_h//40][matrix_w//40] = 1    
        
        
        if white_win or black_win or Game_tie:
            if white_win:
                # gameDisplay.fill((255,255,255))
                gameDisplay.blit(white_win_text,white_win_rect)
            if black_win:
                # gameDisplay.fill((255,255,255))
                gameDisplay.blit(black_win_text,black_win_rect)
            if Game_tie:
                gameDisplay.blit(tie_text,tie_rect)
                
            record_f.write('%s'%Game_Record)
            record_f.write("| \n")
            for row in board_status:
                board_status_f.write('%s'%row)
                board_status_f.write("\n")
            board_status_f.write("\n")
            for j in range(0,len(board_status)):
                for i in range(0,len(board_status[j])):    
                    board_status[j][i]=0
            white_win,black_win = False,False
            RESET =True
            

        if RESET:
            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_r: 
                    gameDisplay.blit(gomoku_board, (0, 0))
                    Game_Record=list()
                    black_current=list()
                    white_current=list()
                    pygame.display.update()
                    white_win,black_win=False,False
                    RESET=False
                    is_white=True
                    
            pygame.display.update()

        if event.type == pygame.QUIT:
            Gaming=False
        if event.type == pygame.MOUSEMOTION and not white_win and not black_win and not RESET:
            pos = pygame.mouse.get_pos()
            pos = Check_pos_inrange(pos,all_location)
            gameDisplay.blit(gomoku_board, (0, 0))
            for pos_white in white_current:
                gameDisplay.blit(white_stone,pos_white)
            for pos_black in black_current:
                gameDisplay.blit(black_stone,pos_black)
            if pos not in black_current and pos not in white_current:
                if is_white:
                    gameDisplay.blit(white_stone,pos)
                else :
                    gameDisplay.blit(black_stone,pos)
            pygame.display.update()


        if event.type == pygame.MOUSEBUTTONUP and not white_win and not black_win and not RESET:
            pos = pygame.mouse.get_pos()
            pos = Check_pos_inrange(pos,all_location)
            if is_white:
                if pos not in white_current and pos not in black_current:
                    white_current.append(list(pos))
                    is_white=False
                    gameDisplay.blit(white_stone,pos)
                    # white_win = check_who_win(white_current)
                    Game_Record.append([1,pos])
            # else:
            #     if pos not in white_current and pos not in black_current:
            #         black_current.append(list(pos))
            #         is_white=True
            #         gameDisplay.blit(black_stone,pos)
            #         # black_win=check_who_win(black_current)
            #         Game_Record.append([0,pos])
            for data in Game_Record:
                tmp = data[1]
                matrix_w,matrix_h=tmp[0],tmp[1]
                matrix_w = matrix_w-17
                matrix_h = matrix_h-8
                if data[0]==0:
                    board_status[matrix_h//40][matrix_w//40] = 2
                else:
                    board_status[matrix_h//40][matrix_w//40] = 1
            
            
            pygame.display.update()        
             
    

record_f.close()
board_status_f.close()
pygame.quit()
quit()