class Demo:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def __str__(self):
        return f"Demo object: {self.name}"

    def __repr__(self):
        return f"Demo(name='{self.name}', values={self.values})"

    def __add__(self, other):
        return self.name + other.name, self.values + other.values

    def __mul__(self, times):
        return self.name * times, self.values * times

    def __eq__(self, other):
        return self.name == other.name and self.values == other.values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __call__(self):
        print(f"Called object: {self.name}")


# Usage
a = Demo("A", [1, 2, 3])
b = Demo("B", [4, 5])

print(a)              # __str__
print(repr(a))        # __repr__

c = a + b             # __add__
print(c)

d = a * 2             # __mul__
print(d)

print(a == b)         # __eq__

print(len(a))         # __len__

print(a[1])           # __getitem__

a()                   # __call__


