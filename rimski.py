num = input()

def decimal_to_roman(n:int):
    d = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI',
            7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',
            40:'XL',50:'L',60:'LX',70:'LXX',80:'LLXXX',90:'XC', 100:'C'}

    ones = n%10
    tens = n-ones
    roman = ''
    if tens > 0:
        roman += d[tens]
    if ones > 0:
        roman += d[ones]
    return roman

def roman_to_decimal(n:str):
    for _ in range(1,100):
        if decimal_to_roman(_) == n:
            return _

def all_chars_same(str1,str2):
    chars_seen = [0]*len(str1)
    cstr2 = [char for char in str2]
    for i in range(len(str1)):
        if str1[i] in cstr2:
            chars_seen[i] = 1
            cstr2.remove(str1[i])
    if chars_seen.count(1) == len(chars_seen):
        return True
    else:
        return False
num2 = roman_to_decimal(num)
mini = ''
for i in range(num2, 0, -1):
    num_test = decimal_to_roman(i)
    if len(num_test) == len(num) and all_chars_same(num,num_test):
        mini = num_test
print(mini)
