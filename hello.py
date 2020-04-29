x = -13

if x > 0:
    print("X is positive")
elif x < 0:
    print("X is negative")
else:
    print("X is 0")

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)

s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)

def square(x):
    return x * x

for i in range(10):
    print("{} squared is {}".format(i, square(i)))
