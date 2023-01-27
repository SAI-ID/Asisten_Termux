def hitung_kmh():
    print('\n====MENGHITUNG KECEPTAN====\n')

    S = float(input("masukan jaraknya : "))
    t = float(input("masukan waktu tempuh : "))

    # rumus adalah v = s/t
    V = S/t

    print("kecepatan anda : ", V, "km/h")