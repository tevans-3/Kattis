import sys

invalid = ['\n', ' ', '+', '-', '=', "=\n"]

def calc(line:list, d:dict):
    try:
        for i in range(len(line)):
            if line[i] not in invalid:
                line[i] = d[line[i]]
        num = eval(" ".join([i for i in line if i != "="][:-1]))
        return num
    except KeyError:
        return -123456789

d  = {}
d2 = {}
for line in sys.stdin:
    line = line.split(" ")
    if line[0] == "def":
        if line[1] in d2.values():
            del d2[d[line[1]]]
            d2[line[2][:-1]] = line[1]
        else:
            d2[line[2][:-1]] = line[1]
        d[line[1]] = line[2][:-1]
    elif line[0] == "calc":
        result = str(calc(line[1:], d))

        if result in d2.keys():
            print(" ".join(line[1:len(line)-1]) + " = " + d2[result])
        else:
           print(" ".join(line[1:len(line)-1]) + " = " + "unknown")
    elif line[0][:-1] == "clear":
        d.clear()
        d2.clear()
