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
	userAns = input("Would you like to continue (Y/N), defaults Y?")
	if(userAns.capitalize() == "N"):
		print("Goodbye!! Hope you enjoyed the game")
		return False
	else:
		return True

# winning sceanrio handling
def declareWinner(markedlist):
	#if one row has all the elements same
	if(' ' not in markedlist) :
		single_row = len(set(markedlist));
		if(single_row == 1):
			return True
		else:
			return False		

#if diagoanls are same
def elementEqualityCheck(listrow1,listrow2,listrow3):
	first_diagoanal_list = [listrow1[0],listrow2[1],listrow3[2]]
	second_diagonal_list =[listrow3[0],listrow2[1],listrow1[2]]
	zeroth_column = [listrow1[0],listrow2[0],listrow3[0]]
	first_column = [listrow1[1],listrow2[1],listrow3[1]]
	second_column = [listrow1[2],listrow2[2],listrow3[2]]
	if(declareWinner(first_diagoanal_list) or declareWinner(second_diagonal_list) or declareWinner(zeroth_column) or declareWinner(first_column) or declareWinner(second_column)) : 
		return True
	else : 
		False	
#calling the functions
userLikesToCont = True 
while  userLikesToCont:
	#initial empty game board view
	renderGameBoard(listRow1,listRow2,listRow3)
	#get the position from user
	selected_position = selectingPosition()
	#get the user input for that postion
	user_input = userInput()
	#update the gameboard with user input and position
	updateGameBoard(selected_position,user_input)
	#display the updated game board and ask to choose again
	renderGameBoard(listRow1,listRow2,listRow3)
	if(declareWinner(listRow1)) :
		userLikesToCont = False
		print("Game won!!");
	elif (declareWinner(listRow2)):
		userLikesToCont = False
		print("Game won!!");
	elif (declareWinner(listRow3)):
		userLikesToCont = False
		print("Game won!!");
	elif (elementEqualityCheck(listRow1,listRow2,listRow3)) :
		userLikesToCont = False
		print("Game won!!");	
	else :
		#ask user if he wants to continue
		userLikesToCont = gameContinue()				
	
#end of while loop
