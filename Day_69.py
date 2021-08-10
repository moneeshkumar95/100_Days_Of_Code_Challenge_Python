print('Day 69: Write a recursive function to output a list '
      'of all the possible  permutations os that string')

def permute(s):
    out = []
    
    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            
            for perm in permute(s[:i] + s[i+1:]):
                print('\nIndex is', i)
                print('Current letter is', let)
                print('perm is', perm)

                out += [let+perm]

                print("Current Output is", out)

    return out

print('\nFinal output:',permute('abc'))0