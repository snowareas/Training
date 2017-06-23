class get_value:
 		def __init__(self,value):
 			self.value = value

a = get_value(3.7)
print(a.value)
b = a
b.value = 4.0
print(a.value)
