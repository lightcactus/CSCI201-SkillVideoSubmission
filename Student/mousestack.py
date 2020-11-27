# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:25:16 2020

@author: krlig
"""
from maze import Maze
from pyliststack import Stack

class Mouse():
    
    def find_maze_paths(self, maze, starting_row, starting_col, exit_row, exit_col):
        
        S=Stack()
        starttuple=(starting_row,starting_col)
        S.push(starttuple)
        
        while S.is_empty() is False:
            current=S.pop()
            #if the exit is reached
            if current[0]==exit_row and current[1]==exit_col:
                maze.set_value(current[0],current[1], maze.THEWAYOUT)
                print("Success!")
                print(maze)
                S=Stack()
                
            elif maze.is_in_maze(current[0],current[1]) and maze.is_clear(current[0],current[1]):
                maze.set_value(current[0],current[1], maze.THEWAYOUT)
                #check to the right
                if maze.is_in_maze(current[0],(current[1]+1)) and maze.is_clear(current[0],(current[1]+1)):
                    newtuple=(current[0],(current[1]+1))
                    S.push(newtuple)
                #check to the left    
                if maze.is_in_maze(current[0],(current[1]-1)) and maze.is_clear(current[0],(current[1]-1)):
                    newtuple=(current[0],(current[1]-1))
                    S.push(newtuple)
                #check above    
                if maze.is_in_maze((current[0]-1),current[1]) and maze.is_clear((current[0]-1),current[1]):
                    newtuple=((current[0]-1),current[1])
                    S.push(newtuple)
                #check below   
                if maze.is_in_maze((current[0]+1),current[1]) and maze.is_clear((current[0]+1),current[1]):
                    newtuple=((current[0]+1),current[1])
                    S.push(newtuple)
                
                