f = list(range(5, 13))
print(f)
for i in range(1, len(f)):
    f[i] **= 2
print(f)

def rotLeft(a, d):
    b = []
    for i in range(-d,len(a) - d):
        b.append(a[i])
    print(b)
    return b
rotLeft(f,2)

def rotRight(a, d):
    b = []
    c = 0
    for i in range(d, len(a)+d):
        if i < len(a):
            b.append(a[i])
        else:
            b.append(a[c])
            c += 1


    print(b)
    return b
rotRight(f,2)