#basic rendering the game board
gameBoardList = ['','','']

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

#function to ask the user to select the position for his input
def selectingPosition():
	position = 'string'
	while not position.isdigit():
		position = input("select the position for the input:");	
		print("please enter a numeric figure (e.g, 1) : ")
	return int(position)
#function to get the user input
def userInput():
	userInput = ""
	allowedInputs = ["O","X"]
	while userInput not in allowedInputs : 
		userInput = input("please enter your prefer mark (O/X) : ")
		userInput = userInput.capitalize()
		print("please enter from allowed ones (O/X)")
		
	return userInput.capitalize()

#calling the functions
rowCount = userGivenRowNo()
#initial empty game board view
gameBoardView(rowCount,gameBoardList)
#get the position from user
selectedPosition = selectingPosition()
#get the user input for that postion
userInput = userInput()

#just a notice
print(f"Notice: the {selectedPosition} from the board will be updaetd with {userInput}")