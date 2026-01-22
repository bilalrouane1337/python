class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b = Book("Python Basics", 200)

print(b.__dict__)
print(b.title)          # normal access
print(b.__dict__['title'])  # dictionary access
