#KAMUS
harga=0
jumlah=0
total=0
bayar=0
kembalian=0

#ALGORITMA
harga = int(input("harga :"))
jumlah = int(input("jumlah barang"))
total = harga*jumlah
print("total:", total)
bayar = int(input("jumlah bayar:"))
kembalian = bayar-total
print("kembalian:",kembalian)