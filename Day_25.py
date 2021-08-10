print('Day 25: Append content of one file to another')

file1 = input('\nEnter the 1st file name: ')
file2 = input('Enter the 2nd file name: ')
#opening both files in read mode
f1 = open(file1, 'r')
f2 = open(file2, 'r')
print(f'\nThe content of file 1: {f1.read()}')
print(f'\nThe content of file 2: {f2.read()}')
#closing both files
f1.close()
f2.close()
#opening 1st file with append mode and 2nd file in read mode
f1 = open(file1, 'a+')
f2 = open(file2, 'r')
f1.write(f2.read())
#moving the cursor at beginning
f1.seek(0)
print(f'\nFile 1 after append:',f1.read())
#closing both files
f1.close()
f2.close()