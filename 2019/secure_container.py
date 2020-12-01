begin = 172851
end = 675869

count = 0



for i in range(begin,end):
    m = []
    sizer = 100000
    for j in range(6):
        m.append(int(i/sizer)%10)
        sizer = sizer/10

    ZERO = 0
    ONE = 0
    TWO = 0
    THREE = 0
    FOUR = 0
    FIVE = 0
    SIX = 0
    SEVEN = 0
    EIGHT = 0
    NINE = 0

    if m[0] <= m[1] <= m[2] <= m[3] <= m[4] <= m[5]:
        #print i
        if m[0]==m[1] or m[1]==m[2] or m[2]==m[3] or m[3]==m[4] or m[4]==m[5]:
            temp = [0,0,0,0,0,0]
            for j in range(6):
                for k in range(6):
                    if m[j] == m[k]:
                        temp[j] += 1
            if 2 in temp:
                count +=1
print count
