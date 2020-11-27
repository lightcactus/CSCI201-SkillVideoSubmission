"""
  Class Maze defines a general structure of a maze
  which consists of a two-dimensional array of characters.
  Each symbol on the maze represents eiehter a possible path
  or a blocker.
 
  Students need to complete this class
  
  Name: Kyle Light
  CSCI 204-01
  Professor: Gutekunst
"""

import random     # random number generator

class Maze:

    def __init__( self, max_row = 12, max_sol = 12 ):
        """Create a maze"""
        self.MAXROW = max_row
        self.MAXCOL = max_sol
        self.POSSIBLEPATH = ' '
        self.BLOCKER      = '*'
        self.THEWAYOUT    = '!'

        self.PATH_BLOCKER_RATIO = 0.5

        self.theMaze = self._gen_maze()

    def _gen_maze( self ):
        """Generate a random maze based on probability"""
        local_maze = [['*' for i in range( self.MAXROW )] \
                         for j in range( self.MAXCOL )]

        for row in range( self.MAXROW ):
            for col in range( self.MAXCOL ):
                threshold = random.random()
                if threshold > self.PATH_BLOCKER_RATIO:
                    local_maze[ row ][ col ] = self.POSSIBLEPATH
                else:
                    local_maze[ row ][ col ] = self.BLOCKER

        return local_maze

    def __str__( self ):
        """Generate a string representation of the maze"""
        
        string=' '
        for i in range(len(self.theMaze[0])):
            string+=str(i%10)
            
        string+='\n'
        
        for row in range(self.MAXROW):
            string=string+str(row%10)
            for col in range(self.MAXCOL):
                string+=self.theMaze[row][col]
            string+='\n'
        
        return string

    def get_col_size( self ):
        """Return column count"""
        return len(self.theMaze[0])

    def get_row_size( self ):
        """Return row count"""
        return len(self.theMaze)

    def read_maze( self, file_name ):
        
        contents=None
        lists=[]
        
        if file_name=='maze1.dat' or file_name=='maze2.dat' or file_name=='maze3.dat' or file_name=='maze4.dat':
            f=open(file_name,'r')
            if f.mode=='r':
                contents=f.read()
            lists=contents.split('\n')
        else:
            self.theMaze=Maze._gen_maze(self)
            return 
            
        new_matrix=[]
        for lines in lists:
            temp_list=[]
            for elements in lines:
                temp_list.append(elements)
            new_matrix.append(temp_list)
                
        new_matrix.pop()
        self.theMaze=new_matrix
        
        
        """Reading maze from a file.
           The file should be in the form of a matrix, e.g.,
           ** *
           *  *
           ** *
           ** *
           would be a 4x4 input maze."""
           
         

    def get_maze( self ):
        """Return a copy of the maze"""
        return self.theMaze


    def is_clear( self, row, col ):
        """Return True if this cell is clear (pathway)."""
        if self.theMaze[row][col]==self.POSSIBLEPATH:
            return True
        else:
            return False
        

    def is_in_maze( self, row, col ):
        """Return True if a cell is inside the maze."""
        if row<0 or col<0:
            return False
        elif row>=self.MAXROW or col>=self.MAXCOL:
            return False
        else:
            return True

    def set_value( self, row, col, value ):
        """Set the value to a cell in the maze."""
        self.theMaze[row][col]=value

    def get_value( self, row, col ):
        """Return the value of the current cell."""
        return self.theMaze[row][col]


