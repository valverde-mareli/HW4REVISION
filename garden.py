def max_flowers(grid):
	if not grid or not grid[0]:
		return 0

	rows = len(grid)
	cols = len(grid[0])
	added = 0

	for r in range(rows):
		for c in range(cols):
			if grid[r][c] != 0:
				continue

			if r > 0 and grid[r - 1][c] == 1:
				continue
			if c > 0 and grid[r][c - 1] == 1:
				continue

			grid[r][c] = 1
			added += 1

	return added
