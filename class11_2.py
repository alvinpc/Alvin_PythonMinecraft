a = [10,25,31]
for i in range(len(a)):
    for j in range(len(a)):
        if a[j] < a[i]:
            t = a[i]
            a[i] = a[j]
            a[j] = t
        print(a)