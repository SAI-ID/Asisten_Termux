from pkg.matematika import mtk




def fungsi_ulang_tambah():
    x = int(input('masukan angka pertama\t: '))
    y = int(input('masukan angka kedua\t: '))
    hasil = mtk.Tambah(x, y)
    print(hasil)

def fungsi_ulang_kurang():
    x = int(input('masukan angka pertama\t: '))
    y = int(input('masukan angka kedua\t: '))
    hasil = mtk.Kurang(x, y)
    print(hasil)
    
def fungsi_ulang_kali():
    x = int(input('masukan angka pertama\t: '))
    y = int(input('masukan angka kedua\t: '))
    hasil = mtk.kali(x, y)
    print(hasil)
    
def fungsi_ulang_bagi():
    x = int(input('masukan angka pertama\t: '))
    y = int(input('masukan angka kedua\t: '))
    hasil = mtk.bagi(x, y)
    print(hasil)

def fungsi_ulang_modulus():
    x = int(input('masukan angka pertama\t: '))
    y = int(input('masukan angka kedua\t: '))
    hasil = mtk.modulus(x, y)
    print(hasil)


def fungsi_ulang_pangkat():
    x = int(input('masukan angka pertama\t: '))
    y = int(input('masukan angka kedua\t: '))
    hasil = mtk.pangkat(x, y)
    print(hasil)