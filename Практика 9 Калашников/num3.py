def sum(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

command = input("Выбери + или -: ")
a = 5
b = 3
if command == "+":
    a1 = sum(a,b)
    print(a1)
elif command == "-":
    a2 = sub(a,b)
    print(a2)
else:
    print("команда не распознана")



