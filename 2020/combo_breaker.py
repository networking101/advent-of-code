pk1 = 12232269
pk2 = 19452773

divisor = 20201227

i = 0
while True:
    if pow(7, i, divisor) == pk1:
        break
    i += 1

print(pow(pk2, i, divisor))