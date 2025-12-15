class Base:
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		self.size = size

	def shape(self):
		return "this is a square"

class Square(Base):
	def __init__(self, x, y, size):
		super().__init__(x, y, size)

	def position(self):
		return (self.x, self.y)

def main():
	s = Square(2, 3, 5)
	print(s.shape())
	print(s.position())
	print(s.size)

main()

