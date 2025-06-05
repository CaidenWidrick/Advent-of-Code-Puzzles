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
    lists_to_check = []
    levels = [int(i) for i in report.split()] #turns line into num list
    lists_to_check.append(levels)

    for i in range(len(levels)):
        tempList = [int(x) for j, x in enumerate(levels) if j is not i]
        lists_to_check.append(tempList)
    
    for testcase in lists_to_check:
        isSafe = crit_check(testcase)
        if isSafe:
            safeReports.append(report)
            break

print(len(safeReports))