def reset_game():
	global board, winner, XO, draw
	time.sleep(3)
	XO = 'x'
	draw = False
	game_initiating_window()
	winner = None
	board = [[None]*3, [None]*3, [None]*3]


game_initiating_window()

while(True):
	for event in pg.event.get():

		if event.type == QUIT:
			pg.quit()
			sys.exit()

		elif event.type is MOUSEBUTTONDOWN:
			user_click()

			if(winner or draw):
				reset_game()

	pg.display.update()
	CLOCK.tick(fps)
