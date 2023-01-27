#pkg import
import os


#pkg local
from pkg import cek_ip_me as ckip
from pkg import cetak as c

try:
    while True:
        try:
            os.system('cls')# ganti clear untuk di termux
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
                    c.fungsi_ulang_tambah()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            c.fungsi_ulang_tambah()
                            p = input('apakah mau keluar(y/n)')
                            
                            
                elif menu_user == '2':                    
                    c.fungsi_ulang_kurang()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            c.fungsi_ulang_kurang()
                            p = input('apakah mau keluar(y/n)')
                
                elif menu_user == '3':                    
                    c.fungsi_ulang_kali()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            c.fungsi_ulang_kali()
                            p = input('apakah mau keluar(y/n)')
        
                elif menu_user == '4':                    
                    c.fungsi_ulang_bagi()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            c.fungsi_ulang_bagi()
                            p = input('apakah mau keluar(y/n)')
        
                elif menu_user == '5':                    
                    c.fungsi_ulang_modulus()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            c.fungsi_ulang_modulus()
                            p = input('apakah mau keluar(y/n)')
        
                elif menu_user == '6':                    
                    c.fungsi_ulang_pangkat()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            c.fungsi_ulang_pangkat()
                            p = input('apakah mau keluar(y/n)')
                else:
                    continue
                
                
            elif i_user == '2':
                print('=== menu')
                print('''
                1). cek ip
                0). keluar
                ''')
                menu_user = input('masukan pilihan\t: ')
                if menu_user == '1':
                    ckip.tampil_ip()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            ckip.tampil_ip()
                            p = input('apakah mau keluar(y/n)')
                
                
                
                
                
                
                        
        except Exception as e:
            print('eror bos', e)
            
            
except Exception as e:
        print('eror bos erornya',e)