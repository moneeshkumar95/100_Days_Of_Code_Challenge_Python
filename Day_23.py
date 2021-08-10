print('Day 23: Reading from & Writing to a Text File')

# ("------------Writing------------")
#Approach 1
with open('test1.txt', 'w') as w:
   w.write('Never Give-up, Keep Moving')
#Approach 2
w = open('test2.txt', 'w')
w.write('Try again Fail again, Fail Better')
w.close()

print("------------Reading------------")
#Approach 1
with open('test1.txt', 'r') as r:
   for line in r:
      print(line)
#Approach 2
r = open('test2.txt', 'r')
print(r.read())
r.close()