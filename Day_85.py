print('Day 85\n')

def solution(lst, target):

    seen = set()

    for num in lst:
        num2 = target - num

        if num2 in seen:
            return True

        seen.add(num)

    return False

print('Output:')
print(solution([1,3,5,1,7],4))
print(solution([1,3,5,1,7],14))