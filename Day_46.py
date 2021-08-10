print('Day 46: Program for Lap Timer\n')

import time

start_time = time.time()
last_time = start_time
lap_num = 1

print("Press Enter to count laps\nPress any button to stop")


while True:
    if input() == '':

        lap_time = round((time.time() - last_time), 2)

        total_time = round((time.time() - start_time), 2)

        print("-" * 20)

        print(f"Lap No: {str(lap_num)}")
        print(f"Total Time: {str(total_time)} Sec")
        print(f"Lap Time: {str(lap_time)} Sec")

        print("-" * 20)

        last_time = time.time()
        lap_num += 1
    else:
        print("\nDone")
        break
