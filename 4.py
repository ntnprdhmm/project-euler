largest = 9009
a = 100
b = 100
while a < 1000:
    b = a
    while b < 1000:
        n = a * b
        s = str(n)
        if s == s[::-1] and n > largest:
            largest = n
        b += 1
    a += 1
print(largest)