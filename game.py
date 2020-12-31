listRow1 = [' ',' ',' ']
listRow2 = [' ',' ',' ']
listRow3 = [' ',' ',' ']


def  renderGameBoard(listRow1,listRow2,listRow3):
	print(f"| {listRow1[0]} | {listRow1[1]} | {listRow1[2]} |")
	print('|___|___|___|')
	print(f"| {listRow2[0]} | {listRow2[1]} | {listRow2[2]} |")
	print('|___|___|___|')
	print(f"| {listRow3[0]} | {listRow3[1]} | {listRow3[2]} |")
	print('|   |   |   |')

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
		listRow1[position-1] = value
	elif(position >3 and position <= 6):
		listRow2[position-4] = value
	elif(position > 6 and position <= 9):
		listRow3[position-7] = value
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

# winning sceanrio handling
def declareWinnerByRow(markedlist):
	#if one row has all the elements same
	if(' ' not in markedlist) :
		single_row = len(set(markedlist));
		if(single_row == 1):
			return True
		else:
			return False		

#if diagoanls are same
def diagoanlWinningCheck(listrow1,listrow2,listrow3):
	first_diagoanal_list = [listrow1[0],listrow2[1],listrow3[2]]
	second_diagonal_list = [listrow3[0],listrow2[1],listrow1[2]]
	if(declareWinnerByRow(first_diagoanal_list) or declareWinnerByRow(second_diagonal_list)) : 
		return True
	else : 
		False	
#calling the functions
userLikesToCont = True 
while  userLikesToCont:
	#initial empty game board view
	renderGameBoard(listRow1,listRow2,listRow3)
	#get the position from user
	selectedPosition = selectingPosition()
	#get the user input for that postion
	user_input = userInput()
	#update the gameboard with user input and position
	updateGameBoard(selectedPosition,user_input)
	#display the updated game board and ask to choose again
	renderGameBoard(listRow1,listRow2,listRow3)
	if(declareWinnerByRow(listRow1)) :
		userLikesToCont = False
		print("Game won!");
	elif (declareWinnerByRow(listRow2)):
		userLikesToCont = False
		print("Game won!");
	elif (declareWinnerByRow(listRow3)):
		userLikesToCont = False
		print("Game won!");
	elif (diagoanlWinningCheck(listRow1,listRow2,listRow3)) :
		userLikesToCont = False
		print("Game won by diagonal!");	
	else :
		#ask user if he wants to continue
		userLikesToCont = gameContinue()				
	
#end of while loop
