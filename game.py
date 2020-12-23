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
	print(gameBoardListRow2)
	print(gameBoardListRow3)

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
def updateGameBoard(position,value):
	if(position <= 3):
		gameBoardListRow1[position-1] = value
	elif(position >3 and position <= 6):
		gameBoardListRow2[position-4] = value
	elif(position > 6 and position <= 9):
		gameBoardListRow3[position-7] = value
	else:
		print("I did not understand! something went wrong!!")

#function to continue or end the game
def gameContinue():
	userAns = "Y"
	userAns = input("Would you like to continue (Y/N)?")
	if(userAns.capitalize() == "N"):
		print("Goodbye!! Hope you enjoyed the game")
		return False
	else:
		return True
#calling the functions
userLikesToCont = True 
while  userLikesToCont:
	#rowCount = userGivenRowNo()
	#initial empty game board view
	renderGameBoard(gameBoardListRow1,gameBoardListRow2,gameBoardListRow3)
	# gameBoardView(rowCount,gameBoardList)

	#get the position from user
	selectedPosition = selectingPosition()
	#get the user input for that postion
	userInput = userInput()
	#update the gameboard with user input and position
	updateGameBoard(selectedPosition,userInput)
	#display the updated game board and ask to choose again
	renderGameBoard(gameBoardListRow1,gameBoardListRow2,gameBoardListRow3)
	#ask user if he wants to continue
	userLikesToCont = gameContinue()
#just a notice
print(f"Notice: position {selectedPosition} from the board will be updaetd with {userInput}")