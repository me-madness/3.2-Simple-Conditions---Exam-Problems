import math

hours = int(input())
days = int(input())
workers = int(input())




work_days = days * 0.9 
overtime_hours = (workers * 2) * work_days
work_hours = work_days * 8 * workers
total_hours = work_hours + overtime_hours

if hours < total_hours:
    print("Yes!{0} hours left.".format(
        math.floor(total_hours - hours)))
else:
    print("Not enough time!{0} hours needed.".format(
        math.floor(hours - total_hours)))