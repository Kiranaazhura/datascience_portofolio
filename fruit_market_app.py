from tabulate import tabulate
headers = ['Index', 'Nama', 'Stock', 'Harga']
DaftarBuah = [['Apel', 20, 10000], ['Jeruk', '15', '15000'], ['Anggur', '25', '20000']]
IsiKeranjang = []
while True:
    print('\t Selamat Datang di Pasar Buah \t\n')
    print("\tList Menu: \n"
        "\t1. Menampilkan Daftar Buah\n"
        "\t2. Menambah Buah\n"
        "\t3. Menghapus Buah\n"
        "\t4. Membeli Buah\n"
        "\t5. Exit Program")
    user_input = int(input(f'\nMasukkan angka Menu yang ingin dijalankan: '))
    if user_input == 1:
        print('\nDaftar Buah\n')
        print(tabulate(DaftarBuah, headers=headers, showindex='always'))
    elif user_input == 2:
        buah_baru = input(f'\nMasukkan Nama Buah: ')
        stock_baru = int(input(f'Masukkan Stock Buah: '))
        harga_baru = int(input(f'Masukkan Harga Buah: '))
        DaftarBuah.append([buah_baru, stock_baru, harga_baru])
        print(tabulate(DaftarBuah, headers=headers, showindex='always'))
    elif user_input == 3:
        print('\nDaftar Buah\n')
        print(tabulate(DaftarBuah, headers=headers, showindex='always'))
        hapus = int(input(f'\nMasukkan index buah yang ingin dihapus: '))
        del DaftarBuah[hapus]
        print(tabulate(DaftarBuah, headers=headers, showindex='always'))
    elif user_input == 4:
        print('\nDaftar Buah\n')
        print(tabulate(DaftarBuah, headers=headers, showindex='always'))
        while True:
            beli = int(input('Masukkan index buah yang ingin dibeli: '))
            jumlah = int(input('Masukkan jumlah yang ingin dibeli: '))
            if jumlah > int(DaftarBuah[beli][1]):
                print(f'Stock tidak cukup, Stock {DaftarBuah[beli][0]} tinggal {DaftarBuah[beli][1]}')
            else:
                IsiKeranjang.append({
                    'nama' : DaftarBuah[beli][0],
                    'qty' : jumlah,
                    'harga' : DaftarBuah[beli][2],
                    'index' : beli
                })
            print('Isi Chart: ')
            print('Nama\t| Qty\t| Harga')
            for item in IsiKeranjang :
                print('{}\t| {}\t| {}'.format(item[0], item[1], item[2]))
            checker = input('Mau beli yang lain? (ya/tidak) = ')
            if(checker == 'tidak') :
                break
        print('Daftar Belanja :')
        print('Nama\t| Qty\t| Harga\t| Total Harga')
        totalHarga = 0
        for item in IsiKeranjang :
            print('{}\t| {}\t| {}\t| {}'.format(item[0], item[1], item[2], item[1] * item[2]))
            totalHarga += item[1] * item[2]    
        while True :
            print('Total Yang Harus Dibayar = {}'.format(totalHarga))
            jmlUang = int(input('Masukkan jumlah uang : '))
            if(jmlUang > totalHarga) :
                kembali = jmlUang - totalHarga
                print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
                for item in IsiKeranjang :
                    DaftarBuah[item['index']]['stock'] -= item['qty']
                IsiKeranjang.clear()
                break
            elif(jmlUang == totalHarga) :
                print('Terima kasih')
                for item in IsiKeranjang :
                    listBuah[item['index']]['stock'] -= item['qty']
                IsiKeranjang.clear()
                break
            else :
                kekurangan = totalHarga - jmlUang
                print('Uang anda kurang sebesar {}'.format(kekurangan))
                
    elif(pilihanMenu == '5') :
        break