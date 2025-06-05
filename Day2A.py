def crit_check(levels:list):
    for i in range(len(levels) - 1):
        num1 = int(levels[i])
        num2 = int(levels[i+1])
        diff = abs(num1 - num2)
        if diff > 3:
            return False
        
    ascList = sorted(levels)
    dscList = sorted(levels, reverse=True)
    if (levels == ascList or levels == dscList) and (len(levels) == len(list(set(levels)))):
        return True
    return False

file = 'input2.txt'
safeReports = []
reports = []

with open(file, 'r') as f:
    content = f.read()
    reports = content.splitlines()

for report in reports: #one report = one line in input
    levels = [int(i) for i in report.split()] #turns line into num list
    isSafe = crit_check(levels)
    if isSafe is True:
        safeReports.append(report)

print(len(safeReports))