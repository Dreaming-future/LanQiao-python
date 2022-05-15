m = ['FFEEFEAAECFFBDBFBCDA',
'DACDEEDCCFFAFADEFBBA',
'FDCDDCDBFEFCEDDBFDBE',
'EFCAAEECEECDCDECADDC',
'DFAEACECFEADCBFECADF',
'DFBAAADCFAFFCEADFDDA',
'EAFAFFDEFECEDEEEDFBD',
'BFDDFFBCFACECEDCAFAF',
'EFAFCDBDCCBCCEADADAE',
'BAFBACACBFCBABFDAFBE',
'FCFDCFBCEDCEAFBCDBDD',
'BDEFCAAAACCFFCBBAAEE',
'CFEFCFDEEDCACDACECFF',
'BAAAFACDBFFAEFFCCCDB',
'FADDDBEBCBEEDDECFAFF',
'CDEAFBCBBCBAEDFDBEBB',
'BBABBFDECBCEFAABCBCF',
'FBDBACCFFABEAEBEACBB',
'DCBCCFADDCACFDEDECCC',
'BFAFCBFECAACAFBCFBAF']

from collections import Counter
c = Counter()
h = {}
for i,x in enumerate(m):
    for j,y in enumerate(x):
        h[y] = h.get(y,0) + 1
print(max(h))
