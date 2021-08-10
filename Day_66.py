print('Day 66: Sentence reversal using algorithm\n')

def rev(sen):
    words = []
    length = len(sen)
    spaces = [' ']
    i = 0

    while i < length:

        if sen[i] not in spaces:
            word_start = i

            while i < length and sen[i] not in spaces:
                i += 1
            words.append(sen[word_start:i])
        i += 1

    return ' '.join(words[::-1])
ip1 = input("Enter a sentence: ")
print("\nReversed sentence:",rev(ip1))