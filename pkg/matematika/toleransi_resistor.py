def r_kalkulet():
    def toleransi(nilai, toler):
        persen = 0
        if (toler == 5):
            persen = 5/100
        elif (toler == 10):
            persen = 10/100
        else:
            print('masukkan 5 atau 10')
        hasil = persen*nilai
        return hasil

    print('='*5, "TOLERANSI RESISTOR", '='*5)

    ohm = int(input('masukan nilai resistor: '))
    print('nilai resistor', ohm, 'Ohm')
    toler = int(input('masukan toleransi: '))
    hasiltoler = toleransi(ohm, toler)
    print('nilai toleransi:', hasiltoler,)
    max = ohm + hasiltoler
    min = ohm - hasiltoler
    print('nilai maksimal:', max, 'ohm')
    print('nilai minimal:', min, 'ohm')