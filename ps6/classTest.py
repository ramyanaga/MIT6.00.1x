class Parent:
    def __init__(self, shift):
        self.shift = shift

class Child(Parent):
    def __init__(self, text):
        Parent.__init__(self, 3)
        self.text = 'hello'

#parent = Parent(3)
child = Child('hello')
print child.shift