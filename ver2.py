listRow1 = [' ',' ',' ']
listRow2 = [' ',' ',' ']
listRow3 = [' ',' ',' ']


def  renderGameBoard(listRow1,listRow2,listRow3):
	print(f"| {listRow1[0]} | {listRow1[1]} | {listRow1[2]} |")
	print('|___|___|___|')
	print(f"| {listRow2[0]} | {listRow2[1]} | {listRow3[2]} |")
	print('|___|___|___|')
	print(f"| {listRow3[0]} | {listRow3[1]} | {listRow3[2]} |")
	print('|   |   |   |')

renderGameBoard(listRow1,listRow2,listRow3)