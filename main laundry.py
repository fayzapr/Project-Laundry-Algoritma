import csv
import os
import time

filename = 'data3.csv'

def hapus_tampilan():
    os.system('cls')

def balik():
    print("\n")
    input("Tekan ENTER untuk kembali ke Menu")
    tampilan()
    menu()

def tampilan():
    print("HF LAUNDRY".center(81))
    print("Tempat Laundry Favorit Anda".center(81))
    print("="*81)
tampilan()

def jenis_layanan():
    print("JENIS LAYANAN".center(81,"-"))
    print(
        "\n [1] Paket Cuci \t\t= Rp 3.500/kg"
        "\n [2] Paket Setrika \t\t= Rp 4.000/kg"
        "\n [3] Paket Cuci Setrika \t= Rp 5.000/kg"
        "\n [4] Paket Express (24 Jam) \t= Rp 8.000/kg"
        )
    print("="*81)
    balik()

def data_diri():
    new = dict()
    new['Nama'] = input("Nama Pemesan\t: ")
    new['Telp'] = int(input("Telp Pemesan\t: "))
    new['Jenis'] = int(input("Jenis Layanan\t: "))
    if new['Jenis'] == 1:
        new['Berat'] = float(input("Berat(kg)\t: "))
        total1 = int(3500 * (new['Berat']))
        new['Total'] = total1
        print("-"*81)
        print("Total Pesanan\t : ", "Rp {:,}".format(total1))
    elif new['Jenis'] == 2:
        new['Berat'] = float(input("Berat(kg)\t: "))
        total2 = int(4000 * (new['Berat']))
        new['Total'] = total2
        print("-"*81)
        print("Total Pesanan\t : ", "Rp {:,}".format(total2))
    elif new['Jenis'] == 3:
        new['Berat'] = float(input("Berat(kg)\t: "))
        total3 = int(5000 * (new['Berat']))
        new['Total'] = total3
        print("-"*81)
        print("Total Pesanan\t : ", "Rp {:,}".format(total3))
    elif new['Jenis'] == 4:
        new['Berat'] = float(input("Berat(kg)\t: "))
        total4 = int(8000 * (new['Berat']))
        new['Total'] = total4
        print("-"*81)
        print("Total Pesanan\t : ", "Rp {:,}".format(total4))
    else:
        print("Angka yang anda masukkan tidak ada dalam layanan.")

    with open(filename, 'a', newline='') as file:
        laundryFile = ['Nama', 'Telp', 'Jenis','Berat', 'Total']
        write = csv.DictWriter(file, fieldnames = laundryFile)
        write.writerow(new)
        print('')
        print("="*81)
        print('HF LAUNDRY'.center(81))
        print("="*81)
    balik()
    

def baca_data():
    total=[]
    totaltr = []
    with open(filename, 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        for row in csvreader:
            total.append(row)
    
    if (len(total) > 0):
        labels = total.pop(0)
        no = "No"
        nomor = 1
        print(f"{no:<10}{labels[0]:<20}{labels[1]:<12}{labels[2]:<10}{labels[3]:<13} {labels[4]:<20}")
        print("-"*81)
        for data in total:
            total2 = int(data[4])
            totaltr.append(total2)
            formated = 'Rp {:,}'.format(total2)
            print(f'{nomor:<10}{data[0]:<20}{data[1]:<12}{data[2]:<10}{data[3]:<13}{formated:<20}')
            nomor += 1
    else:
        print("Tidak ada data!")
    print('-'*81)
    jumlah = sum(totaltr)
    jumlah2 = len(total)
    formated = 'Rp {:,}'.format(jumlah)
    print(f"Jumlah Pelanggan\t\t\t\t\t\t {jumlah2:<5}")
    print(f"Total Transaksi\t\t\t\t\t\t\t {formated:<15}")
    print('-'*81)
    balik()
 
def ubah_pesanan():
    data = []
    data2 = []
    nomor = "No"
    no = 1
    with open(filename, 'r', newline='') as file:
        csvReader = csv.DictReader(file, delimiter=',')
        for row in csvReader:
            data.append(row)
    print("No \t Nama \t Telp \t Jenis \t Berat \t Total") 
    print('-'*81)
    for i in data:
        total2 = int(i['Total'])
        formated = 'Rp {:,}'.format(total2)
        print(
            f"{no}"
            f"\t {i['Nama']}"
            f"\t {i['Telp']}"
            f"\t {i['Jenis']}"
            f"\t {i['Berat']}"
            f"\t", formated
        )
        no += 1
    print('-'*81)
    data3 = int(input("Masukkan nomor urutan : "))
    index = data3 - 1
    data2.append(data[index])
    for elemen in data2:
        elemen['Jenis'] = input("Jenis Layanan\t : ")
        if elemen['Jenis'] == '1':
            harga = 3500
        elif elemen['Jenis'] == '2':
            harga = 4000
        elif elemen['Jenis'] == '3':
            harga = 5000
        elif elemen['Jenis'] == '4':
            harga = 8000
        else:
            print("Jenis layanan ini tidak dapat diubah")
            balik()
        elemen['Berat'] = float(input("Berat(kg)\t : "))
        total = int(harga * int(elemen['Berat']))
        elemen['Total'] = total
        print("Total laundry\t: ","Rp {:,}".format(total))
    with open(filename, 'w', newline='') as file:
        newfile = ['Nama', 'Telp', 'Jenis','Berat', 'Total']
        writer = csv.DictWriter(file, fieldnames=newfile)
        writer.writeheader()
        writer.writerows(data)
        hapus_tampilan()
        print('Pengubahan data berhasil!'.center(81),"\n")
    tampilan()
    baca_data()
    balik()

def hapus_data():
    data = []
    with open(filename, 'r') as file:
        csvReader = csv.DictReader(file, delimiter=',')
        for elemen in csvReader:
            data.append(elemen)
    print("No \t Nama \t Telp \t Jenis \t Berat \t Total") 
    print('-'*81)
    no = 1
    for data2 in data:
        total = int((data2['Total']))
        formated = 'Rp {:,}'.format(total)
        print(
            f"{no}"
            f"\t{data2['Nama']}"
            f"\t{data2['Telp']}"
            f"\t{data2['Jenis']}"
            f"\t{data2['Berat']}"
            f"\t", formated
        )
        no += 1
    print('-'*81)
    no = int(input("Masukkan no : "))
    data.remove(data[no-1])
    print("Data sedang dihapus".center(81,'-')) 
    time.sleep(1)
    with open(filename, 'w', newline='') as file:
        newfile = ['Nama', 'Telp', 'Jenis','Berat', 'Total']
        writer = csv.DictWriter(file, fieldnames=newfile)
        writer.writeheader()
        for new_data in data:
            writer.writerow({'Nama' : new_data['Nama'], 'Telp' : new_data['Telp'], 'Jenis' : new_data['Jenis'], 'Berat' : new_data['Berat'], 'Total' : new_data['Total']})
    hapus_tampilan()
    print('Data Terhapus!'.center(81))  
    tampilan()
    baca_data()
    balik()

def menu():
    print("Pilihan Menu".center(81, "-",))
    print(
        "\n [1] Jenis Layanan"
        "\n [2] Buat Pesanan Baru"
        "\n [3] Ubah Pesanan"
        "\n [4] Hapus Pesanan"
        "\n [5] Laporan Pesanan"
        "\n [6] Keluar"
    )
    print('-'*81)
    menu = int(input('Masukkan angka : '))
    print("="*81)
    print("Permintaan anda kami proses".center(81))
    print("="*81)
    time.sleep(1)

    if menu == 1 :
        hapus_tampilan()
        tampilan()
        jenis_layanan()
    elif menu == 2:
        hapus_tampilan()
        tampilan()
        print("FORM PESANAN BARU".center(81, "-"))
        data_diri()
    elif menu == 3:
        hapus_tampilan()
        tampilan()
        print("UBAH PESANAN".center(81,"-"))
        ubah_pesanan()
    elif menu == 4 :
        hapus_tampilan()
        tampilan()
        print("HAPUS PESANAN".center(81,"-"))
        hapus_data()
    elif menu == 5:
        hapus_tampilan()
        tampilan()
        print("LAPORAN PESANAN".center(81,"-"))
        baca_data()
    elif menu == 6:
        hapus_tampilan()
        print("")
        print("Terima kasih telah mempercayai kami".center(81))
        print("")
        exit()
    else:
        print('Tidak ada dalam Menu')
menu()       