import hashlib

door_id = b"ffykfhsq"
password1 = ""
password2 = ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"]
count = 0
i = 1

while len(password1) < 8 or count < 8:
    hash = hashlib.md5(door_id + str(i).encode())
    res = hash.hexdigest()
    if res[:5] == "00000":
        if len(password1) < 8:
            password1 += res[5]
        if count < 8:
            if res[5].isnumeric() and int(res[5]) < 8 and password2[int(res[5])] == "-1":
                password2[int(res[5])] = res[6]
                count += 1

    i += 1

print(password1)
print(''.join(password2))