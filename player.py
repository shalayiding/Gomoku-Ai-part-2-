import pygame
import numpy as np

def Check_pos_inrange(pos,all_location):
    abs_diff = []
    for location in all_location:
        tmp = []
        tmp=[abs(location[0]-pos[0]),abs(location[1]-pos[1])]
        abs_diff.append(tmp)
    
    return all_location[abs_diff.index(min(abs_diff))]

def check_who_win(current):
    check_horizontal=[]
    check_vertical = []
    check_left_to_right = []
    check_right_to_left=[]


    for data in current:
        tmp = [data[0]+40,data[1]+0]
        while tmp in current:
            check_horizontal.append(tmp)
            tmp = [tmp[0]+40,tmp[1]]
        if len(check_horizontal)>=4:
            return True
        
        tmp = [data[0]+0,data[1]+40]
        while tmp in current:
            check_vertical.append(tmp)
            tmp=[tmp[0],tmp[1]+40]
        if len(check_vertical)>=4:
            return True

        tmp = [data[0]+40,data[1]+40]
        while tmp in current:
            check_left_to_right.append(tmp)
            tmp = [tmp[0]+40,tmp[1]+40]

        tmp = [data[0]+40,data[1]-40]
        while tmp in current:
            tmp = [tmp[0]+40,tmp[1]-40]
            check_right_to_left.append(tmp)
        
        if len(check_left_to_right) >=4:
            return True
        if len(check_right_to_left) >=4:
            return True
            
        check_left_to_right =  list()
        check_right_to_left = list()
        check_vertical=list()
        check_horizontal=list()

    return False
