def count_ways(n):
	if n <1 or n > 30:
		raise ValueError("n must fall between values of 1 and 30")

	if n == 1:
		return 1
	if n == 2:
		return 2
	if n == 3:
		return 4

	a = 1
	b = 2
	c = 4

	for _ in range (4, n + 1):
		total = a + b + c
		a = b
		b = c
		c = total

	return c
