#basic rendering the game board
gameBoardListRow1 = ['','','']
gameBoardListRow2 = ['','','']
gameBoardListRow3 = ['','','']
# function to ask user to provide the row count
def userGivenRowNo():
	#asking user to deciede the size of the game board
	userProvidedRowsCount = input("Please enter the row number : ")
	return int(userProvidedRowsCount)
#function to visualize the game board	
def gameBoardView(rows,gameList):
	noOfRow = 1;
	while noOfRow <= rows:
		print(gameList)
		noOfRow = noOfRow + 1
#static game board rendering
def renderGameBoard(firstRow,secondRow,ThirdRow):
	print(gameBoardListRow1)
	print(gameBoardListRow1)
	print(gameBoardListRow1)

#function to ask the user to select the position for his input
def selectingPosition():
	position = 'string'
	while not position.isdigit():
		position = input("select the position for the input:");	
		if not position.isdigit():
			print("please enter a numeric figure (e.g, 1) : ")
	return int(position)
#function to get the user input
def userInput():
	userInput = ""
	allowedInputs = ["O","X"]
	while userInput.capitalize() not in allowedInputs : 
		userInput = input("please enter your prefer mark (O/X) : ")
		if userInput.capitalize() not in allowedInputs:
			print("please enter from allowed ones (O/X)")
		
	return userInput.capitalize()
#function to update the game board
#def updateGameBoard(position,value):

	
#calling the functions
# rowCount = userGivenRowNo()
#initial empty game board view
renderGameBoard(gameBoardListRow1,gameBoardListRow2,gameBoardListRow3);
# gameBoardView(rowCount,gameBoardList)
#get the position from user
selectedPosition = selectingPosition()
#get the user input for that postion
userInput = userInput()
#update the gameboard with user input and position
#display the updated game board and ask to choose again

#just a notice
print(f"Notice: position {selectedPosition} from the board will be updaetd with {userInput}")