print('Day 57: Find the mirror characters in a '
      'given word\n')

def mirrorChars(w):

    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse =  'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reverse))

    mirror = ''

    for i in range(0, len(w)):
        mirror += dictChars[w[i]]

    return mirror

word = input("Enter the word: ")
print('\nOutput:',mirrorChars(word))