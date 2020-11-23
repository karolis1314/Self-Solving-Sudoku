#Getting the board for sudoku
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#First step we need to select an empty square functions of some sort
#We need a for loop to try numbers
#I need to find the number that fits
#Repeat all of it before it is not valid.
#backtrack if it doesnt

#Check if the current board is valid

#Algorithm backtracking

def solveBoard(bord):
    find = get_empty_square(bord)
    if not find:
        return True
    else:
        row,col=find
    for i in range(1,10):
        if is_valid(bord, i, (row,col)):
            bord[row][col] = i
            
            if solveBoard(bord):
                return True
            
            bord[row][col] = 0
    return False
            
            
            
    
#check if the num is valid
def is_valid(bord, num, pos):
    #Check row
    for i in range(len(bord[0])):
        if bord[pos[0]][i] == num and pos[1] != i:
            return False
    #Check the column verticly
    for i in range(len(bord)):
        if bord[i][pos[1]] == num and pos[0] !=i:
            return False
    #Check the box 1of9 boxes
    box_x = pos[1]//3
    box_y = pos[0]//3
    
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if bord[i][j]==num and (i,j) != pos:
                return False  
    return True
       
#Printing the board    
def print_board(bord):
    for i in range(len(bord)):
        if i % 3 == 0 and i != 0:
            print("-----------")
            
        for j in range(len(bord[0])):
            if j % 3 == 0 and j!=0:
                print("|", end="")
                
            if j == 8:
                print(bord[i][j])
            else:
                print(str(bord[i][j])+"", end="")



#Finding emty space
def get_empty_square(bord):
    for i in range(len(bord)):
        for j in range (len(bord[0])):
            if bord[i][j] == 0:
                return (i,j) #Tumple of row and the column
    return None


print_board(board)
solveBoard(board)
print("_________________________")
print_board(board)