#pkg import
import os


#pkg local
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


try:
    while True:
        try:
            os.system('clear')# ganti clear untuk di termux
            print('='*4, 'SELAMAT DATANG', '='*4)
            print('='*4, 'masukan no pilihan menu')
            print('''
            1). masuk ke menu mtk
            2). masuk ke tool hack
            0). keluar
                ''')
            i_user = input('masukan no pilihan\t: ')
            if i_user == '0':
                break
            elif i_user == '1':
                print('=== menu')
                print('''
                1). Tambah
                2). Kurang
                3). kali
                4). bagi
                5). modulus
                6). pangkat
                0). keluar
                ''')
                menu_user = input('masukan pilihan\t: ')
                
                
                if menu_user == '1':
                    fungsi_ulang_tambah()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            fungsi_ulang_tambah()
                            p = input('apakah mau keluar(y/n)')
                            
                            
                elif menu_user == '2':                    
                    fungsi_ulang_kurang()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            fungsi_ulang_kurang()
                            p = input('apakah mau keluar(y/n)')
                
                elif menu_user == '3':                    
                    fungsi_ulang_kali()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            fungsi_ulang_kali()
                            p = input('apakah mau keluar(y/n)')
        
                elif menu_user == '4':                    
                    fungsi_ulang_bagi()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            fungsi_ulang_bagi()
                            p = input('apakah mau keluar(y/n)')
        
                elif menu_user == '5':                    
                    fungsi_ulang_modulus()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            fungsi_ulang_modulus()
                            p = input('apakah mau keluar(y/n)')
        
                elif menu_user == '6':                    
                    fungsi_ulang_pangkat()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            fungsi_ulang_pangkat()
                            p = input('apakah mau keluar(y/n)')
                else:
                    continue        
        except Exception as e:
            print('eror bos', e)
            
            
except Exception as e:
        print('eror bos erornya',e)