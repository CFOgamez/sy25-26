weight = int(input("choose weight"))
if weight < 100:
    grade = "small"
elif weight <= 200:
    grade = "medium"
else:
    grade = "large"
print(grade)

blemish_counts = []
count = 0
for i in range(5):
    count = count + 1
    number = int(input("Enter the number of blemishes: "))
    blemish_counts.append(number)
total = sum(blemish_counts)
average = total / count
print(total,average)

potatoes = [0, 2, 5, 1, 0, 8, 3, 0]
perfect_potatoes = []
for potato in potatoes:
    if potato == 0:
        perfect_potatoes.append(potato)
    else:
        next
percent =(perfect_potatoes.count(0) / len(potatoes)) * 100

print(percent)