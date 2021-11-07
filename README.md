# labspy02
<p align="center">
<b>Fungsi Perulangan Random dan Contoh Program Perulangan</b>
</p>
<p>

<p align="center">
<img src=""/>
<p align="center">
</p>

<b>A.</b><b>Penjelasan Program Latihan 1#</b><p>
<b>a.</b><b>Menampilan bilangan acak dari bilangan yang lebih kecil dari 0.5<p>
<b>Source Code</b><b>
'''python

while True:
    from random import random
    n=int(input("masukkan bilangan: "))
    for i in range(n):
        while n==n:
            break
        bil=random()%0.5
        print(f"Perulangan ke-{i+1}",bil)
    print("done")
    lanjut=(input("ulangi program??(y/n): "))
    if lanjut=="N" or lanjut=="n":
        break
```