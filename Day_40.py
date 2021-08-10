print('Day 40: Iterate over multiple lists simultaneously')

print("\n-------Approach 1--------")
num = [1, 2, 3]
language = ['Python', 'PHP', 'Java']
framework = ['Django', 'Laravel', 'Spring']

for i, j, k in zip(num, language, framework):
    print(i,j,k)


print("\n-------Approach 2--------")
import itertools
num = [1, 2, 3]
technologies = ['HTML', 'CSS', 'JavaScript']
used_for = ['Structure', 'Presentation', 'Behaviour']

for i, j, k in itertools.zip_longest(num, technologies, used_for):
    print(i,j,k)