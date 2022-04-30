import string

# The function that converts the initial string into a list of lists
def createBoardSpace(input1):
    # Convert the initial string into a list
    list1 = []
    list1[:0] = input1

    # Convert the list of strings into a list of ints
    list2 = [int(i) for i in list1]

    # Convert the int list into a list of lists, with each inner list consisting of 6 ints.
    list3 = [list2[i:i + 6] for i in range(0,len(list2),6)]

    return(list3)

# The function that converts the final list of lists back into a string
def boardSpaceToString(solvedBoardSpace):
    # Convert the list of lists into a single list
    intList = [item for elem in solvedBoardSpace for item in elem]

    # Convert the ints in the list into strings
    stringList = [str(x) for x in intList]

    # Form the final string by iterating over the string list
    finalString = ""
    for val in stringList:
        finalString += val

    return finalString

# The function the finds the empty spaces
def findEmptySpace(boardSpace):
    # Traverse through each row using a nested for loop and find the location containing a 0.
    # The row and column indices for that position are returned.
    for r in range(6):
        for c in range(6):
            if boardSpace[r][c] == 0:
                return r,c

    # If no empty positions are found, return None for both row and column.
    # These values would only be returned when the the soduku is completed.
    return None, None

# The function that checks that each domain value match the constraints
def checkConstraints(boardSpace, domainVal, row, column):
    # Check constraint 1, which is that we cannot have the same value in a row.
    currentRowVals = boardSpace[row]
    if domainVal in currentRowVals:
        return False

    # Check constraint 2, which is that we cannot have the same value in a column.
    currentColVals = [boardSpace[i][column] for i in range(6)]
    if domainVal in currentColVals:
        return False
    
    # Check constraint 3, which is that we cannot have the same value in a 2x3 unit.
    unitRowStart = (row//2) * 2
    unitColStart = (column//3) * 3
    for r in range(unitRowStart, unitRowStart + 2):
        for c in range(unitColStart, unitColStart + 3):
            if boardSpace[r][c] == domainVal:
                return False

    # If the domain val meets all the constraints, return true.
    return True

def solveSudoku(boardSpace):
    # Call the function that finds the first empty space.
    # The function returns the row and column index.
    row, column = findEmptySpace(boardSpace)

    # Check if there are no empty positions left.
    # If there are no empty positions left, the sudoku is complete and is ready to be converted back into a string and printed out.
    if row is None:
        return True

    # Recursively check if the domain val works
    for domainVal in range(1,7):
        if checkConstraints(boardSpace, domainVal, row, column):
            boardSpace[row][column] = domainVal
            if solveSudoku(boardSpace):
                return True
        # If the domain val does not meet the constraints, backtrack.
        boardSpace[row][column] = 0

    # The false here keeps the recursion looping unless the board is solved.
    return False

def main():
    # The infinite while loop allows the program to continue taking inputs.

    while True:
        # Read in the initial board state
        input1 = input()

        if len(input1) == 36:
            # Call the function that takes the input string and converts it into a list of lists. 
            # After the conversion, there will be 6 inner lists inside of a larger list.
            boardSpace = createBoardSpace(input1)

            # Call the function that solves the sudoku puzzle.
            newBoardSpaceBoolean = solveSudoku(boardSpace)

            # This function converts the final 2d board space back into a string.
            solvedString = boardSpaceToString(boardSpace)

            print(solvedString)

if __name__ == "__main__":
    main()