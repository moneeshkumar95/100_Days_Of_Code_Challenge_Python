print('Day 41: Find the second lowest points of the players')

players = [['John', 2.5], ['Mike', -3], ['Albert', 7],
           ['Danny', -3], ['Chris', -1.5], ['Drake', 3.5],
           ['Mark', 0.5], ['Robert', 0], ['Elon', -4.5]]
second_low = 0
n = len(players)

print("\nPlayers Name & Points:")
for i,j in sorted(players):
    print(i,'=',j)
order = sorted(players, key=lambda x: int(x[1]))
for i in range(n):
    if order[i][1] != order[0][1]:
        second_low = order[i][1]
        break
print("\n--Output--\nSecond lowest points:", second_low)
sec_player_name = [x[0] for x in order if x[1] == second_low]
sec_player_name.sort()
print("Players Name: ")
for s_name in sec_player_name:
    print(s_name)
