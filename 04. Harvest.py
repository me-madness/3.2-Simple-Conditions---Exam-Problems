import math

area = int(input())
grapes = float(input())
litre_grapes = int(input())
num_workers = int(input())

vine_for_year = (area * grapes) * 0.40
vine = vine_for_year / 2.5 

if vine > litre_grapes:
    vine_left = vine - litre_grapes
    worker = vine_left / num_workers
    print("Good harvest this year! Total wine: {0} liters.".format(
        math.floor(vine)
    ))
    print("{0} liters left -> {1} liters per person.".format(
        math.ceil(vine_left),
        math.ceil(worker)
    ))
else:
    vine_needed = litre_grapes - vine
    print("It will be a tough winter! More {0} liters wine needed.".format(
        math.floor(vine_needed)
    ))    