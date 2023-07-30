import math

holliday = int(input())

work_days = 365 - holliday
play_time = work_days * 63 + holliday * 127
diference = math.fabs(play_time - 30000)
hourse = math.trunc(diference / 60)
minutes = math.trunc(diference % 60)

if play_time > 30000:
    print("Tom will run away")
    print(f"{hourse} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")    
    print(f"{hourse} hours and {minutes} minutes less for play")