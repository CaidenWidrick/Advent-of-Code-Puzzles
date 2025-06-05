import re
file = 'input3.txt'

with open(file, 'r') as f:
    content = f.read()

pattern = r"(mul\(\d{1,3},\d{1,3}\))"

matches = re.findall(pattern, content)

total = 0
for match in matches:
    mulNums = [int(x) for x in re.findall(r"(\d{1,3})", match)]
    total += mulNums[0] * mulNums[1]

print(total)