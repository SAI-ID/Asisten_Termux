#pkg import
import os
import time

#pkg local
from pkg import cek_ip_me as ckip
from pkg.matematika import toleransi_resistor as tr
from pkg.matematika import mtk
from pkg import ytdow
from pkg.matematika import rumus_kecepatan as rk
from pkg import cetak as c



def bersihkan_console():
    os.system('clear') # ganti clear untuk di termux
    
def keluar_trm():
    os.system('exit')

try:
    while True:
        try:
            bersihkan_console()
            print('='*4, 'SELAMAT DATANG', '='*4)
            print('='*4, 'masukan no pilihan menu')
            print('''
            1). masuk ke menu mtk
            2). masuk ke tool hack
            3). kelistrikan
            4.) yt downloder
            0). keluar
                ''')
            i_user = input('masukan no pilihan\t: ')
            if i_user == '0':
                break
            
            elif i_user == '212':
                mtk.ss()
                time.sleep(5)
                bersihkan_console()
            
            elif i_user == '1':
                bersihkan_console()
                print('=== menu')
                print('''
                1). Tambah
                2). Kurang
                3). kali
                4). bagi
                5). modulus
                6). pangkat
                7). kecepatan km/h
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
                
                elif menu_user == '7':
                    bersihkan_console()
                    rk.hitung_kmh()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            bersihkan_console()
                            rk.hitung_kmh()
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
                
            elif i_user == '3':
                print('=== menu')
                print('''
                1). cek toleransi resistor
                0). keluar
                ''')
                menu_user = input('masukan pilihan\t: ')
                if menu_user == '1':
                    bersihkan_console()
                    tr.r_kalkulet()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            bersihkan_console()
                            tr.r_kalkulet()
                            p = input('apakah mau keluar(y/n)')
                
            elif i_user == '4':
                print('=== menu')
                print('''
                1). download mp4
                2). download mp3
                0). keluar
                ''')
                menu_user = input('masukan pilihan\t: ')
                if menu_user == '1':
                    bersihkan_console()
                    ytdow.mulai_download()
                    p = input('apakah mau keluar(y/n)')
                    if p == 'y':
                        continue
                    else:
                        while p == 'n':
                            bersihkan_console()
                            ytdow.mulai_download()
                            p = input('apakah mau keluar(y/n)')
                
                elif menu_user == '2':
                    bersihkan_console()
                    print('dalam pengembangan....!')
                    for i in range(1, 5):
                        time.sleep(1)
                        print(f'keluar dalam...{i} ')
                    continue
        except Exception as e:
            print('eror bos', e)
            
            
except Exception as e:
        print('eror bos erornya',e)
