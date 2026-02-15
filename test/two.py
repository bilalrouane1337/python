lst = [1, 2, 3]
lst.append(5)

print(id(lst[0]))

t = tuple(lst)

print(id(t[0]))
