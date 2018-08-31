# Written by Boxuan, Hu for COMP9021


import sys

def single_transport(n):
    if new_fish_1[n][1] < expect_kg:
        quantity = new_fish_1[n+1][0] - new_fish_1[n][0] + expect_kg - new_fish_1[n][1] # distance + needed
        new_fish_1[n+1][1] = new_fish_1[n+1][1] - quantity
        new_fish_1[n][1] = expect_kg
    elif new_fish_1[n][1] > expect_kg:
        quantity = new_fish_1[n][1] - expect_kg
        if quantity > new_fish_1[n+1][0] - new_fish_1[n][0]:
            new_fish_1[n+1][1] = new_fish_1[n+1][1] + quantity - (new_fish_1[n+1][0] - new_fish_1[n][0])# quantity - distance
            new_fish_1[n][1] = expect_kg
        elif quantity <= new_fish_1[n+1][0] - new_fish_1[n][0]:
            new_fish_1[n][1] = expect_kg
    else:
        None
        

        
try:
    filename = str(input('Which data file do you want to use? '))
    with open(filename) as File:
        fish = File.readlines()
    fish = [x.strip('\n') for x in fish]
    fish = [x.strip(' ') for x in fish]
    lenth = len(fish)
except FileNotFoundError:
    sys.exit()
        
km = []
kg = []
new_fish = []
new_fish_1 = [[0,0] for _ in range(lenth)]
for i in range(lenth):
    new_fish.append(fish[i].split())

for i in range(lenth):
    for j in range(2):
        new_fish_1[i][j] += int(new_fish[i][j])
        

new_fish_1.sort()
max_of_fish = 0

for i in range(lenth):
    max_of_fish += int(new_fish[i][1])
    km.append(int(new_fish[i][0]))
    kg.append(int(new_fish[i][1]))
    

max_of_fish = max_of_fish // lenth
min_of_fish = min(kg)
expect_kg = (max_of_fish + min_of_fish) // 2


while True:
    for n in range(lenth - 1):
        single_transport(n)

    sum_of_fish = 0
    for i in range(lenth):
        sum_of_fish += new_fish_1[i][1]

    if sum_of_fish == expect_kg * lenth:
        break

    elif sum_of_fish < expect_kg * lenth:
        max_of_fish = expect_kg
        expect_kg = (min_of_fish + max_of_fish) // 2
        for i in range(lenth):
            new_fish_1[i][1] = kg[i]
    elif sum_of_fish > expect_kg * lenth:
        min_of_fish = expect_kg
        expect_kg = (min_of_fish + max_of_fish) // 2
        if min_of_fish == expect_kg:
            break
        for i in range(lenth):
            new_fish_1[i][1] = kg[i]
            

print(f'The maximum quantity of fish that each town can have is {new_fish_1[0][1]}.')




