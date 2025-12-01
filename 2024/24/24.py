with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

flag = False
solved = {}
gates = {}

max_z = 0

for line in lines:

    if not line:
        flag = True
    elif flag:
        left, right = line.split(" -> ")
        gates[right] = left.split()
        if right[0] == 'z' and int(right[1:]) > max_z:
            max_z = int(right[1:])

    else:
        left, right = line.split(": ")
        solved[left] = int(right)

def recurse(curr):
    if curr in solved:
        return solved[curr]
    
    a, calc, b = gates[curr]

    if a not in solved:
        a = recurse(a)
    else:
        a = solved[a]
    if b not in solved:
        b = recurse(b)
    else:
        b = solved[b]
    
    if calc == 'AND':
        res = a & b
    elif calc == 'OR':
        res = a | b
    elif calc == 'XOR':
        res = a ^ b
    else:
        assert(False)

    solved[curr] = res
    return res

# calculate z output
x = 0
y = 0
for k, v in solved.items():
    if k[0] == 'x':
        x += v << int(k[1:])
    if k[0] == 'y':
        y += v << int(k[1:])
z = x + y
print(x, y, z)

silver = 0
for k, v in gates.items():
    if k[0] == 'z':
        solved[k] = recurse(k)
        silver += solved[k] << int(k[1:])
print(silver)

# silver = 0
# for k, v in gates.items():
#     if k[0] == 'z':
#         tmp = recurse(k)
#         print(k, tmp)
#         if tmp << int(k[1:]) != z & (1 << int(k[1:])):
#             print("INCORRECT")
#             pass
#         solved[k] = tmp
#         silver += tmp << int(k[1:])
# print(silver)



swapped = [("svm", "nbc"), ("kqk", "z15"), ("fnr", "z39"), ("z23", "cgq")]
# swapped = [(), (), (), ()]
for s in swapped:
    if not s:
        continue
    a, b = s
    tmp = gates[a]
    gates[a] = gates[b]
    gates[b] = tmp

gold =  [x for y in swapped for x in y]
gold.sort()

print(','.join(gold))



# solved by hand
# z00 = x00 XOR y00

# z01 = wbd XOR dqq
# wbd = x00 AND y00
# dqq = x01 XOR y01

# z02 = vnc XOR msc
# vnc = kwk OR  mhb
# kwk = wbd AND dqq
# mhb = y01 AND x01
# msc = y02 XOR x02

# z03 = prb XOR rvw
# prb = wdv OR  mcc
# wdv = msc AND vnc
# mcc = y02 AND x02
# rvw = x03 XOR y03

# z04 = rcw XOR nfp
# nfp = bhr OR  bbq
# bbq = prb AND rvw
# bhr = x03 AND y03
# rcw = x04 XOR y04

# z05 = rgq XOR svm
# rgq = ppw OR  brg
# brg = nfp AND rcw
# ppw = x04 AND y04
# svm = y05 AND x05	swap with nbc


# z14 = mdg XOR tbd
# tdb = dhr OR  phn
# phn = ttw AND ckr
# dhr = x13 AND y13
# mdg = y14 XOR x14

# z15 = dkk OR  pbd	z15 = fwr XOR cpv	swap kqk with z15
# dkk = y15 AND x15	cpv = wfh OR wth
# pbd = cpv AND fwr	wth = mdg AND tdb
# fwr = x15 XOR y15	wfh = x14 AND y14
# 			fwr = x15 XOR y15

# z16 = kqk XOR rbr	z16 = kqk XOR rbr
# cpv = wfh OR  wth	kqk = dkk OR  pbd
# kqk = fwr XOR cpv	pdb = cpv AND fwr
# fwr = x15 XOR y15	dkk = y15 AND x15
# rbr = x16 XOR y16	rbr = x16 XOR y16

# z17 = gcc XOR dhd
# gcc = bbm OR  qbc
# bbm = rbr AND kqk
# qbc = y16 AND x16
# dhd = x17 XOR y17


# z22 = nnw XOR smn
# nnw = brb OR  rjf
# rjf = mkw AND cqf
# brb = x21 AND y21
# smn = x22 XOR y22

# z23 = x23 AND y23	z23 = kph XOR hpw	swap z23 and cgq
# 			kph = jcb OR dwt
# 			jcb = smn AND nnw
# 			dwt = x22 AND y22
# 			hpw = y23 XOR x23

# z24 = nkr XOR ngq
# nkr = x24 XOR y24
# ngq = qdg OR  cgq
# qdg = hpw AND kph
# cgq = kph XOR hpw


# z37 = jqt XOR jjs
# jqt = rwt OR tsn
# tsn = fwh AND tnk
# rwt = y36 AND r36
# jjs = x37 XOR y37

# z38 = gsb XOR pgb
# pgb = qpr OR  rbm
# rbm = jqt AND jjs
# qpr = x37 AND y37
# gsb = y38 XOR x38

# z39 = fsp AND bdr	z39 = bdr XOR fsp	swap z39 and fnr
# fsp = hpf OR  phv	fsp = hpf OR  phv
# hpf = pgb AND gsb	hpf = pgb AND gsb
# phv = x38 AND y38	phv = x38 AND y38
# bdr = y39 XOR x39	bdr = y39 XOR x39

# z40 = nqp XOR sbn	z40 = nqp XOR sbn
# sbn = fnr OR  nrj	sbn = fnr OR  nrj
# fnr = bdr XOR fsp	fnr = fsp AND bdr
# nrj = x39 AND y39	nrj = x39 AND y39
# nqp = y40 XOR x40	nqp = y40 XOR x40

# z41 = kfv XOR jmc
# kfv = bnb OR  fpq
# bnb = nqp AND sbn
# fpq = x40 AND y40
# jmc = x41 XOR y41

# z42 = vsd XOR cdq
# vsd = psj OR  qpv
# psj = jmc AND kfv
# qpv = x41 AND y41
# cdq = y42 XOR x42

# z43 = jjm XOR pcj
# pcj = sbh OR  tcr
# sbh = cdq AND vsd
# tcr = y42 AND x42
# jjm = x43 XOR y43

# z44 = ggt XOR mjm
# mjm = tkj OR  kdt
# kdt = jjm AND pcj
# tkj = x43 AND y43
# ggt = X44 XOR y44

# z45 = sgk OR  hww
# sgk = mjm AND ggt
# mjm = tkj OR  kdt
# hww = x44 AND y44
# ggt = x44 XOR y44
