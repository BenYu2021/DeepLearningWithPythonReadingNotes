class Man:
    def __init__(self, name):
        self.name = name;
        print("initialized")

    def hello(self):
        print("hello " + self.name + "!")

    def goodbye(self):
        print("goodbye " + self.name + "!")


m = Man("David")  # PEP 8: E305 expected 2 blank lines after class or function definition, found 1
m.hello()
m.goodbye()
