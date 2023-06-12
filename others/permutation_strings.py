from itertools import permutations as pm

a = 'bb9be7aa'
b = 'e8b94f2e89c'
c = 'b74bdfb0e144'
d = '4394eae0a1'
e = '6eb125f8546'
f = 'cd45f85bc29c'

l = [list(i) for i in pm('abcdef')]

for ind1, val1 in enumerate(l):
    for ind2, val2 in enumerate(val1):
        match val2:
            case 'a':
                l[ind1][ind2] = a
            case 'b':
                l[ind1][ind2] = b
            case 'c':
                l[ind1][ind2] = c
            case 'd':
                l[ind1][ind2] = d
            case 'e':
                l[ind1][ind2] = e
            case 'f':
                l[ind1][ind2] = f

l = [''.join(i) for i in l]

for i in l:
    print(i)
print(len(l))
