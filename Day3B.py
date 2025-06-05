import re
file = 'input3.txt'

with open(file, 'r') as f:
    content = f.read()

split_by_do = content.split("do()")
do_parts = " "
for section in split_by_do:
    split_on_dont = section.split("don't()")
    do_part = split_on_dont.pop(0)
    do_parts += do_part
    

pattern = r"(mul\(\d{1,3},\d{1,3}\))"

matches = re.findall(pattern, do_parts)

total = 0
for match in matches:
    mulNums = [int(x) for x in re.findall(r"(\d{1,3})", match)]
    total += mulNums[0] * mulNums[1]

print(total)