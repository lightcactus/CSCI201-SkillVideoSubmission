# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:44:09 2020

Name: Kyle Light
CSCI 204-01
Professor: Gutekunst
"""
from maze import Maze

class Mouse():
        
    def find_maze_paths(self, maze, cur_row, cur_col, exit_row, exit_col):
        
        if cur_col==exit_col and cur_row==exit_row:
            maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
            print(maze)
            return
        else:
            #Check to see if the exit is below current position
            if cur_row<exit_row:
                #Check to see what direction we can go in
                if maze.is_in_maze((cur_row+1),cur_col)==True and maze.is_clear((cur_row+1),cur_col)==True:
                    maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
                    cur_row+=1
                
                elif maze.is_in_maze(cur_row,(cur_col+1))==True and maze.is_clear(cur_row,(cur_col+1))==True:
                    maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
                    cur_col+=1
                    
                elif maze.is_in_maze(cur_row,(cur_col-1))==True and maze.is_clear(cur_row,(cur_col-1))==True:
                    maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
                    cur_col=cur_col-1
            
            #Check to see if the exit is above
            elif cur_row>exit_row:
                #Check to see what direction we can go in
                if maze.is_in_maze((cur_row-1),cur_col)==True and maze.is_clear((cur_row-1),cur_col)==True:
                    maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
                    cur_row=cur_row-1
                
                elif maze.is_in_maze(cur_row,(cur_col+1))==True and maze.is_clear(cur_row,(cur_col+1))==True:
                    maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
                    cur_col+=1
                    
                elif maze.is_in_maze(cur_row,(cur_col-1))==True and maze.is_clear(cur_row,(cur_col-1))==True:
                    maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
                    cur_col=cur_col-1
                    
            elif cur_row==exit_row:
                if cur_col<exit_col and maze.is_in_maze(cur_row,(cur_col+1))==True and maze.is_clear(cur_row,(cur_col+1))==True:
                    maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
                    cur_col+=1
                    
                elif cur_col>exit_col and maze.is_in_maze(cur_row,(cur_col-1))==True and maze.is_clear(cur_row,(cur_col-1))==True:
                    maze.set_value(cur_row,cur_col,maze.THEWAYOUT)
                    cur_col=cur_col-1
                    
            return Mouse.find_maze_paths(self, maze, cur_row, cur_col, exit_row, exit_col)
                
                    
        
        
        
        
    
    