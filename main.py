while True:
	
	if get_pos_y() == 0 and get_pos_x() == 1:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(West)
	
	if get_pos_x() < 2:
		if get_pos_y() < 2:
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(North)
		elif get_pos_y() == 2:
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(East)
	else:
		if get_pos_x() == 2:
			if can_harvest():
				harvest()
				plant(Entities.Grass)
				move(South)
		if get_pos_y() == 0:
			if can_harvest():
				harvest()
				plant(Entities.Grass)
				move(West)