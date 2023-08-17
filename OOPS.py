class Item:
	def calculate(self, x, y ):
		assert  x >=10 , f"value is less than ten and the value is {x}"
		assert y >= 10, f"value is less than ten and the value is {y}"
		return x*y+x/y
	def __init__(self):
		print("Object is created using constructor")


iteam1 = Item()
print(iteam1.calculate(109, 90))
