in_str = input().lower()

d = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3', 'f':'#',
        'g':'6', 'h':'[-]', 'i':'|', 'j':'_|', 'k':'|<', 'l':'1',
        'm':'[]\/[]', 'n':'[]\[]', 'o':'0', 'p':'|D', 'q':'(,)',
        'r':'|Z', 's':'$', 't':"']['", 'u':'|_|', 'v':'\/', 'w':'\/\/',
        'x':'}{', 'y':"`/", 'z':'2', ' ': ' '}
out_str = []
for char in in_str:
    if char in d.keys():
        out_str.append(d[char])
    else:
        out_str.append(char)
print("".join(out_str))
