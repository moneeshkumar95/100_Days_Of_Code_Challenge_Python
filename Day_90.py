print('Day 90\n')

print("-------------Approach 1-------------")

K = 4
N = 3
list1 = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]

res = [ele for ele in list1 if ele.count(K) == N]

print(f'The original list is : {list1}')
print(f'Filtered tuples : {res}')


print("\n-------------Approach 2-------------")
K = 5
N = 2
list2 = [(8, 5, 6, 5), (4, 5, 3), (2, 5, 5)]

res = [ele for ele in list2 if sum(cnt == K for cnt in ele) == N]

print(f'The original list is : {list2}')
print(f'Filtered tuples : {res}')