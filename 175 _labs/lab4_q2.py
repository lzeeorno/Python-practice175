from lab4_input_maze import Maze, MazeSquare
from lab4_input_Stack import Stack 

#creat a maze, let player deicide which maze they want to go in
player_command = input('please input the maze you want to go in (a or b): ')
if player_command == 'a':
    maze = Maze("lab4_input_solvable_maze.txt")
    
elif player_command == 'b':
    maze = Maze("lab4_input_unsolvable_maze.txt")
    

#initialize a stack 
moves_stack = Stack()

#add the start square to the stack 
current_position = maze.get_start_square()
moves_stack.push(current_position)

#repeat the following aslong as the stack is not empty
while not moves_stack.is_empty():
    #pop a square of the stack(current square)
    current_position = moves_stack.pop()
    
    #if the current square is the finish square, the solution has been found
    if maze.is_finish_square(current_position):
        break
    
    #otherwise, get the list of squares which can be moved to from current square, and add them to stack 
    available_moves = current_position.get_legal_moves()
    for move in available_moves:
        moves_stack.push(move)
        
        
#### display result
if maze.is_finish_square(current_position):
    print("Solution have been found!")
else:
    print("NO Solution!")
        