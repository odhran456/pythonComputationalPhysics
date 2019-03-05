print("Hello World!")
x = "Hello "
y = "World! "
z = x + y
print(z)


one = 1
two = 2
three = one + two
print(three)

print(str(three)+" "+z)


number1 = 3
number2 = 3.0
a = 7 / number1
b = 7 / number2


names=["Paddy","Rita","Eoin","Emanuele"]
names.append("Caoimhe")
print(names[4])
names.insert(2,"Odhran")
print(names[3])


factor = 2
while factor < 35:
    if 35 % factor == 0:
        print(35,"is divisible by", factor)
        break
    else:
        factor = factor + 1
else: print(35,"is prime.")


for name in names:
    print(name)

for name in range(0,4):
    print(name)


a = 1
b = 1
while b < 20:
    print(a)
    a,b = b,a+b #simultaneous variable assignments


fname = "John"
age = 23
if fname == "John" and age == 23:
    print("name: John, age: 23")
if fname == "John" or fname == "Mary":
    print("name: Either John or Mary")
