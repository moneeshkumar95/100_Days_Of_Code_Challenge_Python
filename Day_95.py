print('Day 95\n')

print("Task 1: Integer to Roman Numeral")
def int_to_roman(num):
    n = num
    val = [1000, 900, 500, 400,
           100, 90, 50, 40, 10,
           9, 5, 4, 1]

    syb = ['M', 'D', 'CM', 'CD',
           'C', 'XC', 'L', 'XL',
           'X', 'IX', 'V', 'IV',
           'I']

    roman_num = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return f'Input = {num} & Output = {roman_num}'

print(int_to_roman(14))
print(int_to_roman(1200))
print(int_to_roman(756))


print("\n\nTask 2: Roman Numeral to Integer")
def roman_to_int(s):
    rom_val = {'I':1, 'V':5,'IX':10,
               'X':10, 'L':50, 'C':100,
               'D':500, 'M':1000}
    int_val = 0

    for i in range(len(s)):

        if i > 0 and rom_val[s[i]] > rom_val[s[i-1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i-1]]
        else:
            int_val += rom_val[s[i]]

    return f'Input = {s} & Output = {int_val}'

print(roman_to_int('LM'))
print(roman_to_int('XLDM'))
print(roman_to_int('LDIXM'))







