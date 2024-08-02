import sys

n = int(input())

d = {}

end = 0

for line in sys.stdin:
    words_in_line = []
    word = ""

    if end:
        n = int(line.split()[0])

    if line == "EndOfText\n":
        srtd = []
        for key in d:
            if d[key] == n:
                srtd.append(key)
        srtd.sort()
        for wd in srtd:
            print(wd)
        if len(srtd) == 0:
            print("There is no such word.")
        print()
        d.clear()
        end = 1
    else:
        end = 0

    for char in line:
        ch = char.lower()
        if ch in "abcdefghijklmnopqrstuvwxyz":
            word += ch
        elif word != "" and word != "endoftext":
            words_in_line.append(word)
            word = ""
    for wd in words_in_line:
        if wd in d.keys():
            d[wd] += 1
        else:
            d[wd] = 1
