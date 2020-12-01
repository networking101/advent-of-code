import hashlib

text = b"iwrupvqb"
count = 0
result = "1"

result = hashlib.md5(text + str(count).encode("utf-8"))

result = result.digest()

print(result)
print(result[2])

while result[:3] != b"\x00\x00\x00":
    if count % 100000 == 0:
        print(count)
    #print(text + str(count).encode("utf-8"))
    #print(result.digest()[:5])
    count += 1
    result = hashlib.md5(text + str(count).encode("utf-8"))

    result = result.digest()

print(result)
print(count)
