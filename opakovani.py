import random

import statistics

pole = [3, 5, 8, 1, 2, 4, 6, 7,]


pole_sorted = sorted(pole)

print (pole_sorted)


pole_sorted_reverse = sorted(pole, reverse=True)

print (pole_sorted_reverse)


sumarize = sum(pole)

prumerna_hodnota = sumarize/len(pole)

print (prumerna_hodnota)

 
for i in range(0, len(pole)):
    for j in range(i+1, len(pole)):
        if pole[i] >= pole[j]:
            pole[i], pole[j] = pole[j],pole[i]

print (pole)


for i in range(0, len(pole)):
    for j in range(i+1, len(pole)):
        if pole[i] <= pole[j]:
            pole[i], pole[j] = pole[j],pole[i]

print(pole)


total_sum = 0
misto_pole = 0

while misto_pole < len(pole): 
    total_sum = total_sum + pole[misto_pole] 
    misto_pole += 1
  
prumerna_hodnota_without_sum = total_sum/len(pole)

print (prumerna_hodnota_without_sum)



pole_random = []

rand_range=8

for i in range(rand_range):
    pole_random.append(random.randint(1,100))
print(pole_random)


pole_random_max = max(pole_random)

print (pole_random_max)


pole_random_min = min(pole_random)

print (pole_random_min)


pole_random_median = statistics.median(pole_random)

print (pole_random_median)