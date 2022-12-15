# for loop examples

alphabets = ["one", "two", "three", "four", "five", "six"]
for x in alphabets:
    if x == "three":
        break
    print(x)

for n in alphabets:
    if n == "two":
        continue
    print(n)

for y in range(5, 10):
    print(y)
for z in range(5, 10, 3):
    print(z)
else:
    print("completed")