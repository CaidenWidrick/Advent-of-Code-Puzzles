def count_apprncs(num=int, l2=list):
    counter = 0
    for item in l2:
        if item == num:
            counter += 1
    return counter

file = "input1.txt"
l1 = []
l2 = []
with open(file, 'r') as f:
    content = f.read()
    lines = content.splitlines()

    for line in lines:
        line = line.strip()
        pair = line.split()
        l1.append(int(pair[0]))
        l2.append(int(pair[1]))

totalSim = 0

for num in l1:
    apprncs = int(count_apprncs(int(num), l2))
    iterSim = apprncs * num
    totalSim += iterSim

print(totalSim)