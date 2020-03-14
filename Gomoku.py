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
for i in range(17,width,40):
    for j in range(8,height,40):
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
white_win_rect = white_win_text.get_rect()
black_win_rect = black_win_text.get_rect()
white_win_rect.center = (width//2,height//2)
black_win_rect.center = (width//2,height//2)
#setting game record file and list 
Game_Record = []
record_f = open("Game_record.txt","a")
RESET = False
Gomoku_AI.Create_random_move(all_location)
#board 
board_status = []

for j in range(8,height,40):
    tmp = []
    for i in range(17,width,40):    
        tmp.append(0)
    board_status.append(tmp)
print(len(board_status))

while Gaming:
    # for data in test_data:
    #     gameDisplay.blit(black_stone,data)
    
    for event in pygame.event.get():
        # print(event)
        
        #update_board_status 
        

        if white_win or black_win :
            if white_win:
                # gameDisplay.fill((255,255,255))
                gameDisplay.blit(white_win_text,white_win_rect)
            if black_win:
                # gameDisplay.fill((255,255,255))
                gameDisplay.blit(black_win_text,black_win_rect)
            record_f.write('%s'%Game_Record)
            record_f.write("| \n")
            white_win,black_win = False,False
            RESET =True
            pygame.display.update()

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
                    white_win = check_who_win(white_current)
                    Game_Record.append([1,pos])
            else:
                if pos not in white_current and pos not in black_current:
                    black_current.append(list(pos))
                    is_white=True
                    gameDisplay.blit(black_stone,pos)
                    black_win=check_who_win(black_current)
                    Game_Record.append([0,pos])
            pygame.display.update()        
             
    
    
record_f.close()
pygame.quit()
quit()