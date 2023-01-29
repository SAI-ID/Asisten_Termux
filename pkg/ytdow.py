def mulai_download():
    from pytube import YouTube
    print('='*4, 'yt downloder by siro', '='*4)
    print('\n')
    # Meminta link video dari pengguna
    link = input("Masukkan link video YouTube\t: ")

    # Membuat objek YouTube
    yt = YouTube(link)

    # Menampilkan semua pilihan kualitas video yang tersedia
    streams = yt.streams.filter(file_extension='mp4')
    for i, stream in enumerate(streams):
        print(f"{i+1}. {stream.resolution} {stream.abr}kbps")

    # Meminta pilihan kualitas video dari pengguna
    pilihan = int(input("Pilih kualitas video yang diinginkan (masukkan nomor): "))

    # Mengunduh video dengan kualitas yang dipilih
    stream = streams[pilihan-1]
    stream.download(output_path='/sdcard/Download')
    print('sukses di download cek di folder download anda')