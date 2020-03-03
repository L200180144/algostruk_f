def formatRupiah(x):
    a = str(x)
    b = ""
    i = -1
    while i >= -len(a):
        if ((i+1)%3 == 0 and (i+1) != 0):
            b = "." + b
        b = a[i] + b
        i-=1
    return "Rp "+b
