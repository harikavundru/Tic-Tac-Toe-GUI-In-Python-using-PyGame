def drawXO(row, col):
	global board, XO

	# for the first row, the image
	# should be pasted at a x coordinate
	# of 30 from the left margin
	if row == 1:
		posx = 30

	# for the second row, the image
	# should be pasted at a x coordinate
	# of 30 from the game line
	if row == 2:

		# margin or width / 3 + 30 from
		# the left margin of the window
		posx = width / 3 + 30

	if row == 3:
		posx = width / 3 * 2 + 30

	if col == 1:
		posy = 30

	if col == 2:
		posy = height / 3 + 30

	if col == 3:
		posy = height / 3 * 2 + 30

	# setting up the required board
	# value to display
	board[row-1][col-1] = XO

	if(XO == 'x'):

		# pasting x_img over the screen
		# at a coordinate position of
		# (pos_y, posx) defined in the
		# above code
		screen.blit(x_img, (posy, posx))
		XO = 'o'

	else:
		screen.blit(o_img, (posy, posx))
		XO = 'x'
	pg.display.update()


def user_click():
	# get coordinates of mouse click
	x, y = pg.mouse.get_pos()

	# get column of mouse click (1-3)
	if(x < width / 3):
		col = 1

	elif (x < width / 3 * 2):
		col = 2

	elif(x < width):
		col = 3

	else:
		col = None

	# get row of mouse click (1-3)
	if(y < height / 3):
		row = 1

	elif (y < height / 3 * 2):
		row = 2

	elif(y < height):
		row = 3

	else:
		row = None

	# after getting the row and col,
	# we need to draw the images at
	# the desired positions
	if(row and col and board[row-1][col-1] is None):
		global XO

		drawXO(row, col)
		check_win()
