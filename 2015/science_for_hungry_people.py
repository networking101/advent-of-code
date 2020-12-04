with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

data = {}

for line in lines:
    a = line.split()
    data[a[0][:-1]] = [int(a[2][:-1]), int(a[4][:-1]), int(a[6][:-1]), int(a[8][:-1]), int(a[10])]

ca = []
du = []
fl = []
te = []
cal = []

for i in data:
    ca.append(data[i][0])
    du.append(data[i][1])
    fl.append(data[i][2])
    te.append(data[i][3])
    cal.append(data[i][4])

vals = []

sum1 = 0
for i in range(100):
    sum1 = i
    for j in range(100):
        sum2 = sum1 + j
        if sum2 > 100:
            break
        for k in range(100):
            sum3 = sum2 + k
            if sum3 > 100:
                break
            for l in range(100):
                if (sum3 + l) < 100:
                    continue
                if (sum3 + l) > 100:
                    break

                a = ca[0] * i + ca[1] * j + ca[2] * k + ca[3] * l
                b = du[0] * i + du[1] * j + du[2] * k + du[3] * l
                c = fl[0] * i + fl[1] * j + fl[2] * k + fl[3] * l
                d = te[0] * i + te[1] * j + te[2] * k + te[3] * l

                e = cal[0] * i + cal[1] * j + cal[2] * k + cal[3] * l

                if e != 500:
                    continue

                if a < 0:
                    a = 0
                if b < 0:
                    b = 0
                if c < 0:
                    c = 0
                if d < 0:
                    d = 0

                vals.append(a * b * c * d)

print(max(vals))
