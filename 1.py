from math import fmod
sum = 0
for i in range(3, 1000):
    if fmod(i, 3) == 0 or fmod(i, 5) == 0:
	sum = sum + i
print(sum)
