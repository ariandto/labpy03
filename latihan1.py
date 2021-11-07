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