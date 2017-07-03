class MyClass:
    """A simple example class"""

    def __init__(self, a = 0, b = 0):
		self.a = a
		self.b = b 
		
    def f(self):
        return 'hello world'

		
x, y  = MyClass(3,4), MyClass()
print x.a , y.a
print x.b, y.b

print x.f()
print x.__doc__