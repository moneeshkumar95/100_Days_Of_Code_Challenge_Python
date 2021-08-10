print('Day 18: Converting list of tuples into dictionaries')

print("\n------------Approach 1------------")
top_lang = [('Python','1st'),('JavaScript','2nd'),('C/C++','3rd'),
            ('JAVA','4th'),('PHP','5th')]
print( f'Input: {top_lang}')
print( f'\nOutput: {dict(top_lang)}')

print("\n------------Approach 2------------")
def DictConv(tups):
    conv = {}
    for a,b in tups:
        conv.setdefault(a,b)
    return conv

top_framework = [('Django','1st'),('Express','2nd'),('Rails','3rd'),
                 ('Laravel','4th'),('Spring','5th')]
print( f'Input: {top_framework}')
print( f'\nOutput: {DictConv(top_framework)}')