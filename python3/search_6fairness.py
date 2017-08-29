import itertools
import sys
sys.path.append('.')
import time
import datetime
import fairness

currfile = 'current6.txt'
statfile = 'statlog6.txt'



def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(itertools.islice(iterator, n, n), None)

def silnia(x):
    if x == 0:
        return 1
    else:
        return x * silnia(x-1)


def log(cntA, cntB, cntC, cntD, cntE, cntF, cnt):
    tmp = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") + ' (A,B,C,D,E,F) => (' + str(cntA) + ',' + str(cntB) + ',' + str(cntC) + ',' + str(cntD) + ',' +str(cntE) + ',' + str(cntF) + ') -> No.' + str(cnt) 
    # print info
    print(tmp)
    # save info to log
    fs = open(statfile, 'a')
    fs.write(tmp + "\n")
    fs.close()
    # save current state
    fcur = open(currfile, 'w')
    fcur.write(str(cntA) + '\n')
    fcur.write(str(cntB) + '\n')
    fcur.write(str(cntC) + '\n')
    fcur.write(str(cntD) + '\n')
    fcur.write(str(cntE) + '\n')
    fcur.write(str(cntF) + '\n')
    fcur.close()

#init vectors
a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 9, 10, 11, 12]
c = [13, 14, 15, 16, 17, 18]
d = [19, 20, 21, 22, 23, 24]
e = [25, 26, 27, 28, 29, 30]
f = [31, 32, 33, 34, 35, 36]


# simple report (head + 4 rows)
'''
head, row1, row2, row3, row4 = [],[],[],[],[]
print('Permutation identifiers for each quad numbers:')
print('Column A:')
cnt = 0
for v in itertools.permutations(a):
    head.append(cnt)
    row1.append(v[0])
    row2.append(v[1])
    row3.append(v[2])
    row4.append(v[3])
    cnt += 1
perm_report(head, row1, row2, row3, row4)
row1, row2, row3, row4 = [],[],[],[]

print('Column B:')
cnt = 0
for v in itertools.permutations(b):
    row1.append(v[0])
    row2.append(v[1])
    row3.append(v[2])
    row4.append(v[3])
    cnt += 1
perm_report(head, row1, row2, row3, row4)
row1, row2, row3, row4 = [],[],[],[]

print('Column C:')
cnt = 0
for v in itertools.permutations(c):
    row1.append(v[0])
    row2.append(v[1])
    row3.append(v[2])
    row4.append(v[3])
    cnt += 1
perm_report(head, row1, row2, row3, row4)
row1, row2, row3, row4 = [],[],[],[]

print('Column D:')
cnt = 1
for v in itertools.permutations(d):
    row1.append(v[0])
    row2.append(v[1])
    row3.append(v[2])
    row4.append(v[3])
    cnt += 1
perm_report(head, row1, row2, row3, row4)
row1, row2, row3, row4 = [],[],[],[]

print('Column E:')
cnt = 0
for v in itertools.permutations(e):
    row1.append(v[0])
    row2.append(v[1])
    row3.append(v[2])
    row4.append(v[3])
    cnt += 1
perm_report(head, row1, row2, row3, row4)
row1, row2, row3, row4 = [],[],[],[]

print('Column F:')
cnt = 0
for v in itertools.permutations(f):
    row1.append(v[0])
    row2.append(v[1])
    row3.append(v[2])
    row4.append(v[3])
    cnt += 1
perm_report(head, row1, row2, row3, row4)
head, row1, row2, row3, row4 = [],[],[],[],[]
'''

cnt = 0
cntA = 0
cntB = 0
cntC = 0
cntD = 0
cntE = 0
cntF = 0

startcntA = 0
startcntB = 0
startcntC = 0
startcntD = 0
startcntE = 0
startcntF = 0

# or use command line to pass arguments
if len(sys.argv) == 7:
    print("Recovering state...")
    startcntA = int(sys.argv[1])
    startcntB = int(sys.argv[2])
    startcntC = int(sys.argv[3])
    startcntD = int(sys.argv[4])
    startcntE = int(sys.argv[5])
    startcntF = int(sys.argv[6])
else:
    print("Read state from file ...")
    fc = open(currfile, 'r')
    startcntA = int(fc.readline())
    startcntB = int(fc.readline())
    startcntC = int(fc.readline())
    startcntD = int(fc.readline())
    startcntE = int(fc.readline())
    startcntF = int(fc.readline())
    fc.close()

'''
genA = itertools.permutations(a)
consume(genA, startcntA)
cntA = startcntA

genB = itertools.permutations(b)
consume(genB, startcntB)
cntB = startcntB

genC = itertools.permutations(c)
consume(genC, startcntC)
cntC = startcntC

genD = itertools.permutations(d)
consume(genD, startcntD)
cntD = startcntD

genE = itertools.permutations(e)
consume(genE, startcntE)
cntE = startcntE

genF = itertools.permutations(f)
consume(genF, startcntF)
cntF = startcntF

print('Starting from saved state:')

v = next(genA)
row1.append(v[0])
row2.append(v[1])
row3.append(v[2])
row4.append(v[3])
v = next(genB)
row1.append(v[0])
row2.append(v[1])
row3.append(v[2])
row4.append(v[3])
v = next(genC)
row1.append(v[0])
row2.append(v[1])
row3.append(v[2])
row4.append(v[3])
v = next(genD)
row1.append(v[0])
row2.append(v[1])
row3.append(v[2])
row4.append(v[3])
v = next(genE)
row1.append(v[0])
row2.append(v[1])
row3.append(v[2])
row4.append(v[3])
v = next(genF)
row1.append(v[0])
row2.append(v[1])
row3.append(v[2])
row4.append(v[3])
perm_report(head, row1, row2, row3, row4)
print()
'''

genA = itertools.permutations(a)
consume(genA, startcntA)
cntA = startcntA

genB = itertools.permutations(b)
consume(genB, startcntB)
cntB = startcntB

genC = itertools.permutations(c)
consume(genC, startcntC)
cntC = startcntC

genD = itertools.permutations(d)
consume(genD, startcntD)
cntD = startcntD

genE = itertools.permutations(e)
consume(genE, startcntE)
cntE = startcntE

genF = itertools.permutations(f)
consume(genF, startcntF)
cntF = startcntF

cnt = cntA*silnia(len(b))*silnia(len(c))*silnia(len(d))*silnia(len(e))*silnia(len(f)) + cntB*silnia(len(c))*silnia(len(d))*silnia(len(e))*silnia(len(f)) + cntC*silnia(len(d))*silnia(len(e))*silnia(len(f)) +cntD*silnia(len(e))*silnia(len(f)) + cntE*silnia(len(f)) + cntF
cntEnd = silnia(len(a))*silnia(len(b))*silnia(len(c))*silnia(len(d))*silnia(len(e))*silnia(len(f))
#cnt = cntA*silnia(len(a))*silnia(len(b))*silnia(len(c_d_e)) + cntB*silnia(len(b))*silnia(len(c_d_e)) + cntCDE*silnia(len(c_d_e)) + cntF
print('PERMUTATION ' + str(cnt) + '/' + str(cntEnd) + ' RESTORED')

#log(cntA, cntB, cntC, cntD, cntE, cntF, cnt)

# 4,4,4,4,4,4
for va in genA:
    for vb in genB:
        for vc in genC:
            for vd in genD:
                for ve in genE:
                    log(cntA, cntB, cntC, cntD, cntE, cntF, cnt)
                    for vf in genF:
                        diceset = [
                            [ va[0], vb[0], vc[0], vd[0], ve[0], vf[0], 61-vf[0], 61-ve[0], 61-vd[0], 61-vc[0], 61-vb[0], 61-va[0] ],
                            [ va[1], vb[1], vc[1], vd[1], ve[1], vf[1], 61-vf[1], 61-ve[1], 61-vd[1], 61-vc[1], 61-vb[1], 61-va[1] ],
                            [ va[2], vb[2], vc[2], vd[2], ve[2], vf[2], 61-vf[2], 61-ve[2], 61-vd[2], 61-vc[2], 61-vb[2], 61-va[2] ],
                            [ va[3], vb[3], vc[3], vd[3], ve[3], vf[3], 61-vf[3], 61-ve[3], 61-vd[3], 61-vc[3], 61-vb[3], 61-va[3] ],
                            [ va[4], vb[4], vc[4], vd[4], ve[4], vf[4], 61-vf[4], 61-ve[4], 61-vd[4], 61-vc[4], 61-vb[4], 61-va[4] ],
                            [ va[5], vb[5], vc[5], vd[5], ve[5], vf[5], 61-vf[5], 61-ve[5], 61-vd[5], 61-vc[5], 61-vb[5], 61-va[5] ]
                        ]
                        #print(str(diceset))
                        fairness.fairness(diceset)
                        cnt += 1
                        cntF += 1
                    genF = itertools.permutations(f)
                    cntF = 0
                    cntE += 1
                genE = itertools.permutations(e)
                cntE = 0
                cntD += 1
            genD = itertools.permutations(d)
            cntD = 0
            cntC += 1
        genC = itertools.permutations(c)
        cntC = 0
        cntB += 1
    genB = itertools.permutations(b)
    cntB = 0
    break  # permutations of column A does not needed; it is the end

print('END')
