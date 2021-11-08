# labspy02
<p align="center">
Fungsi Perulangan Random dan Contoh Program Perulangan
</p>
<p>

<p align="center">
<img src=""/>
<p align="center">
</p>

A. Penjelasan Program Latihan 1#<p>
a. Menampilkan bilangan acak dari bilangan yang lebih kecil dari 0.5<p>
Source Code:</p>

```python
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
Hasil Program sebagai berikut<p>

<p align="center">
<img src="https://github.com/ariandto/labpy03/blob/main/Looping/L1.png"/>
<p align="center">
</p>




Keterangan</p>

```python
while True:
```
- Berarti loop selamanya. Pernyataan mengambil ekspresi dan mengeksekusi tubuh loop sementara mengevaluasi ekspresi (boolean) "benar".Trueselalu mengevaluasi ke boolean "true" dan dengan demikian mengeksekusi badan perulangan tanpa batas.<p>

```python
from random import random
```

- Perbedaan<p>
```import random```<p>

mengimpor modul acak yang berisi berbagai hal yang berkaitan dengan pembuatan angka acak. Diantaranya adalah random () fungsi yang menghasilkan angka acak antara 0 dan 1.<p>
Melakukan impor dengan cara ini mengharuskan Anda menggunakan sintaks random.random().Fungsi acak juga dapat diimpor dari modul secara terpisah<p>

```from random import random```<p>

Hal ini memungkinkan Anda untuk kemudian hanya memanggil random() langsung.<p>

* Untuk sekedar informasi jika ingin eksekusi dengan library modul ```from random import random``` harus menggunakan IDE atau text editor `pycharm`

```print(f"Perulangan ke-{i+1}",bil)```<p>

* Merupakan looping yang berfungsi untuk menampilkan sequence dari bilangan yang ditampilkan<p>