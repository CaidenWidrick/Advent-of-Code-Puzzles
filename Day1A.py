file = "input1.txt"
listOne = []
listTwo = []
with open(file, 'r') as f:
    content = f.read()
    lines = content.splitlines()

    for line in lines:
        line = line.strip()
        pair = line.split()
        listOne.append(int(pair[0]))
        listTwo.append(int(pair[1]))

listOne.sort()
listTwo.sort()

totalDiff = 0
for n1, n2 in zip(listOne, listTwo):
    diff = abs(n1 - n2)
    totalDiff += diff

print(totalDiff)
#print(listOne)
#print(listTwo)