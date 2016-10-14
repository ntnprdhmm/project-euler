from math import fmod
sum = 2
x = 1
y = 2
f = 3
while f < 4000000:
    if fmod(f, 2) == 0:
        sum = sum + f
    x = y
    y = f
    f = x + y
print(sum)
