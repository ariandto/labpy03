<p align="center">
Fungsi Perulangan Random dan Contoh Program Perulangan
</p>
<p>

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
- Berarti loop selamanya. Pernyataan mengambil ekspresi dan mengeksekusi tubuh loop sementara mengevaluasi ekspresi (boolean) "benar". True selalu mengevaluasi ke boolean "true" dan dengan demikian mengeksekusi badan perulangan tanpa batas.<p>

```python
from random import random
```

- Perbedaan<p>
```import random```<p>

mengimpor modul acak yang berisi berbagai hal yang berkaitan dengan pembuatan angka acak. Diantaranya adalah random () fungsi yang menghasilkan angka acak antara 0 dan 1.<p>
Melakukan impor dengan cara ini mengharuskan Anda menggunakan sintaks random.random(). Fungsi acak juga dapat diimpor dari modul secara terpisah<p>

```from random import random```<p>

Hal ini memungkinkan Anda untuk kemudian hanya memanggil random() langsung.<p>

```print(f"Perulangan ke-{i+1}",bil)```<p>

* Merupakan looping yang berfungsi untuk menampilkan sequence dari bilangan yang ditampilkan<p>

B. Penjelasan Program Latihan 2#<p>

Source Code:</p>

```python
while True:
    loop=int(input("masukkan bilangan: "))
    if loop==0:
        break
```
* Hasil Program<p>

<p align="center">
<img src="https://github.com/ariandto/labpy03/blob/main/Looping/L3.png"/>
<p align="center">
</p>

- Keterangan</p>

- ```while True``` dihentikan dengan ```if loop==0``` yang berarti jika user input angka 0 maka program akan berakhir<p>

C. Penjelasan Program Latihan 3#<p>

Buat program sederhana dengan perulangan: ​program1.py
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan
modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada
bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5,
pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan
keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8
bulan berjalan usahanya<p>

Source code awal:

```python
modal = 100000000
for x in range(1, 9):
    if (x >= 1 and x <= 2):
        b = modal * 0
        print("Laba bulan ke- ", x, ":", b)
    if (x >= 3 and x <= 4):
        c = modal * 0.1
        print("Laba bulan ke- ", x, ":", c)
    if (x >= 5 and x <= 7):
        d = modal * 0.5
        print("Laba bulan ke- ", x, ":", d)
    if (x == 8):
        e = modal * 0.2
        print("Laba bulan ke- ", x, ":", e)
print()
```

#Hasil:
<p align="center">
<img src="https://github.com/ariandto/labpy03/blob/main/Looping/LABA1.png"/>
<p align="center">
</p>

- Source code tahap kedua dengan acuan total berdasarkan looping yang dihasilkan

```python
modal = 100000000
for x in range(1, 9):
    if (x >= 1 and x <= 2):
        b = modal * 0
        print("Laba bulan ke- ", x, ":", b)
    if (x >= 3 and x <= 4):
        c = modal * 0.1
        print("Laba bulan ke- ", x, ":", c)
    if (x >= 5 and x <= 7):
        d = modal * 0.5
        print("Laba bulan ke- ", x, ":", d)
    if (x == 8):
        e = modal * 0.2
        print("Laba bulan ke- ", x, ":", e)
print()
total=b+b+c+c+d+d+d+e
print("Total laba: ",total)
```
<p align="center">
<img src="https://github.com/ariandto/labpy03/blob/main/Looping/lb1.png"/>
<p align="center">
</p>

- Keterangan</p>
jika hanya input ```total=b+c+d+e``` maka tidak sesuai program perulangan yang ditampilkan pada source code awal. ```total=b+b+c+c+d+d+d+e```

- Terima Kasih
