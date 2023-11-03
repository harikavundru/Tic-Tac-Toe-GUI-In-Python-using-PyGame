def check_win():
	global board, winner, draw

	# checking for winning rows
	for row in range(0, 3):
		if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
			winner = board[row][0]
			pg.draw.line(screen, (250, 0, 0),
						(0, (row + 1)*height / 3 - height / 6),
						(width, (row + 1)*height / 3 - height / 6),
						4)
			break

	# checking for winning columns
	for col in range(0, 3):
		if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
			winner = board[0][col]
			pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
						((col + 1) * width / 3 - width / 6, height), 4)
			break

	# check for diagonal winners
	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

		# game won diagonally left to right
		winner = board[0][0]
		pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):

		# game won diagonally right to left
		winner = board[0][2]
		pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

	if(all([all(row) for row in board]) and winner is None):
		draw = True

	draw_status()
