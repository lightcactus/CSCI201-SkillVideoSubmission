Name: Kyle Light

My work followed the guidelines given in the project with no extra methods or classes created.
The only notable difference in my work is that i use tuples in my mousestack class.
My mouststack file allows for the user to find the best possible path through a maze using stacks.

TEST: maze1.dat

Enter the name of the maze file ("none" if  using random file): maze1.dat
maze1.dat
-------- The Original Maze --------
 012345678901
0*** ********
1***    *****
2*** **  ****
3***   *  ***
4***** ** ***
5***** ** ***
6***** ******
7*****   ****
8***   * ****
9*   **  ****
0* *    *****
1* **********


Please enter the starting row : 2
2

Please enter the starting column : 3
3

Please enter the exiting row : 11
11

Please enter the exiting column : 1
1
Success!
 012345678901
0*** ********
1***    *****
2***!**  ****
3***!!!*  ***
4*****!** ***
5*****!** ***
6*****!******
7*****!!!****
8***!!!*!****
9*!!!**!!****
0*!*!!!!*****
1*!**********

TEST: maze2.dat

Enter the name of the maze file ("none" if  using random file): maze2.dat
maze2.dat
-------- The Original Maze --------
 012345678901
0************
1***    *****
2*** **  ****
3***   *  ***
4***** ** ***
5***** ** ***
6***** ******
7*****   ****
8****  * ****
9*   **  ****
0* *    *****
1************


Please enter the starting row : 1
1

Please enter the starting column : 3
3

Please enter the exiting row : 10
10

Please enter the exiting column : 1
1
Success!
 012345678901
0************
1***!   *****
2***!**  ****
3***!!!*  ***
4*****!** ***
5*****!** ***
6*****!******
7*****!!!****
8****!!*!****
9*!!!**!!****
0*!*!!!!*****
1************

TEST: maze3.dat

Enter the name of the maze file ("none" if  using random file): maze3.dat
maze3.dat
-------- The Original Maze --------
 012345678901
0* *  * **** 
1**  **  ** *
2 ********   
3**   * *   *
4*  **     **
5****  ****  
6 *  * * *  *
7 *    ****  
8 *   ** * **
9  ** ***  * 
0 * * * *    
1 ***  ***   


Please enter the starting row : 2
2

Please enter the starting column : 9
9

Please enter the exiting row : 7
7

Please enter the exiting column : 5
5
Success!
 012345678901
0* *  * **** 
1**  **  ** *
2 ********!  
3**   *!*!! *
4*  **!!!!!**
5**** !****  
6 *  *!* *  *
7 *   !****  
8 *   ** * **
9  ** ***  * 
0 * * * *    
1 ***  ***   

TEST: maze4.dat

Enter the name of the maze file ("none" if  using random file): maze4.dat
maze4.dat
-------- The Original Maze --------
 012345678901
0************
1            
2*********** 
3            
4 ***********
5            
6*********** 
7            
8 ***********
9            
0*********** 
1            


Please enter the starting row : 1
1

Please enter the starting column : 0
0

Please enter the exiting row : 11
11

Please enter the exiting column : 0
0
Success!
 012345678901
0************
1!!!!!!!!!!!!
2***********!
3!!!!!!!!!!!!
4!***********
5!!!!!!!!!!!!
6***********!
7!!!!!!!!!!!!
8!***********
9!!!!!!!!!!!!
0***********!
1!!!!!!!!!!!!

This test is interesting because it tests the ability of the find_maze_paths function
to take the longest possible path from enterance to exit.

