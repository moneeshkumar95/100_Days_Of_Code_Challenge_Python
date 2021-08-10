print('Day 73: Check if 3 given lengths form a '
      'right-angled triangle\n')


def right_angle_check(n):
    x,y,z = sorted(n)

    if x**2 + y**2 == z**2:
        print("It form a right-angled triangle\n")

    else:
        print("It doesn't form the right angle triangle\n")

num = list(map(int, input("Enter the 3 lengths: ").split()))
right_angle_check(num)

num1 = list(map(int, input("Enter the 3 lengths: ").split()))
right_angle_check(num1)

num2 = list(map(int, input("Enter the 3 lengths: ").split()))
right_angle_check(num2)

num3 = list(map(int, input("Enter the 3 lengths: ").split()))
right_angle_check(num3)