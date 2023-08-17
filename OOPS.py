class Item:

	def calculate(self, x: int, y):
		assert x >= 10, f"value is less than ten and the value is {x}"
		assert y >= 10, f"value is less than ten and the value is {y}"
		return x*y+x/y
	def __init__(self):
		print("Object is created using constructor")
iteam1 = Item()
print(iteam1.calculate(10, 10))

# simple inheritance
class Monster:
	def __init__(self, health, energy):
		self.health = health
		self.energy = energy
	def attack(self, amount):
		print("Monster was attacked")
		print(amount,"damage occurs ")
		# self.energy -= amount
		# print(f"the remaining health {Monster.energy}")
	def move(self, speed):
		print("the monster has moved")
		print("It have a speed of ", speed)

class Shark(Monster):
	def __init__(self, speed):
		self.speed = speed
	def bite(self):
		print("Shark has successfully attacked")
mon = Monster(100, 69)
shark1 = Shark(120)
shark1.bite()
shark1.attack(20)
shark1.move(122)  # accessing parent element
