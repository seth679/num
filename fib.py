n = int(input())
a = [0, 1]
for i in range(2, n):
    a.append((a[i - 1] + a[i - 2]))
l = 0
c = 0
 for i in range(0, n):
    c = c + 1
    if (c > l):
        l = l + 1
        c = 0
if (c > 0):
    l = l + 1
    c = 0
sp = l - 1
for i in range(0, l):
    for k in range(sp):
        print(' ', end=' ')
    for j in range(0, i + 1):
        if (c == n):
            break
        print(a[c], ' ', end=' ')
        c = c + 1
    print('\n')
    sp = sp - 1


