with open("input.txt", "r") as fp:
	lines = [line.strip() for line in fp]

print(lines)

cnt = 0
tl = []

for line in lines:
	
	"""
	if not line:
		cnt += len(tl)
		tl = []
		continue
	"""
	if not line:
		for i in tl[0]:
			cond = True
			for j in tl:
				if i not in j:
					cond = False
			if cond == True:
				cnt += 1
		tl = []
		print(cnt)
		continue	

	"""
	for i in line:
		if i not in tl:
			tl.append(i)
	"""

	tl.append(line)


#cnt += len(tl)

for i in tl[0]:
	cond = True
	for j in tl:
		if i not in j:
			cond = False
	if cond == True:
		cnt += 1
print(cnt)

print(cnt)
