# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:18:32 2021

@author: sadib
"""
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


def solution(b):
    
    finder = empty_search(b)
    if not finder:
        return True
    else:
        row, col = finder
     
    for i in range(1,10):          
        if check_valid(b, i, (row, col)):    
            b[row][col] = i  # If the number in this position works, we add it to our board.
            
            if solution(b):  # Here we recursively call the solution function, which helps us solve this sudoku really fast, using backtracking.
                return True
            
            b[row][col] = 0
            
            
    return False

def check_valid(b, number, position):
    
    # This for loop will check if the number is already in the row
    for i in range(len(b[0])):     
        if b[position[0]][i] == number and position[1] != 1:
            return False

    # This for loop will check if the number is already in the column
    for i in range(len(b)):
        if b[i][position[1]] == number and position[0] != 1:
            return False

    # Check 3x3 square to see if the number is already in it
    box_1 = position[1] // 3
    box_2 = position[0] // 3
    
    for i in range(box_2 * 3, box_2*3 + 3 ):
            for k in range(box_1 * 3, box_1*3 + 3 ):
                if b[i][k] == number and (i,k) != position:
                    return False


    return True

def print_function(b):
    for i in range(len(b)):
        if i % 3 == 0 and i!= 0:
              
            print("--------------------------") #Seperates the board every 3 rows  
        for k in range(len(b[0])):
            if k % 3 ==0 and k != 0:
                print(" | ", end ="") #Seperates the board every 3 columns
                    
            if k ==8:
                print(b[i][k])
            else:
                print(str(b[i][k]) + " ", end="")

def empty_search(b):
    for i in range(len(b)):
        for k in range(len(b[0])):
            if b[i][k] == 0 :
                return (i, k)

    return None                    
                



print_function(board)
solution(board)
print("-----------------------------")
print("the board above is the board you started with")
print("                             ")
print("the board below is the solution")
print("-----------------------------")
print_function(board)