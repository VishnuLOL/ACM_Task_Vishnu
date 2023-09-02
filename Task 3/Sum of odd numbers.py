n = eval(input("Enter list:"))
l = []
for i in n:
    if i % 2 != 0:
        l.append(i)
print(sum(l))
