print('''\nDay 32: Find minimum number of platforms required in a 
        railway station given the arrival & departure time\n''')

def platform(arr, dep):
    #sorting the arr & dep
    arr.sort(), dep.sort()
    platform_need, result, i = 1,1,1
    j = 0

    while (i < len(arr)) and (j < len(dep)):
        #if a train arrives before a train departure
        if arr[i] <= dep[j]:
            platform_need += 1
            i += 1
        # if a train arrives after a train departure
        elif arr[i] > dep[j]:
            platform_need -= 1
            j += 1
        if platform_need > result:
            result = platform_need
    return result
arrival = [6.15, 6.35, 6.45, 7.05, 7.15, 7.35]
departure = [6.25, 6.55, 7.05, 7.25, 7.45, 7.55]

print( f'Input:\nArrival = {arrival}\nDeparture = {departure}\n\nOutput:')
print('Minimum number of platform required:',platform(arrival,departure))