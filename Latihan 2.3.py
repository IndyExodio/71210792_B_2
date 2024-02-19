gaji = eval(input(f"Gaji per jam                   = "))
jam = eval(input(f"Jumlah Jam Kerja Pada 1 Minggu = "))
print("======================================================")
hasil = gaji * jam * 5
print(f"Hasil Gaji Selama 5 Minggu adalah {hasil:,}")
print("======================================================")
pajak = hasil * 14 / 100
gaji_bersih = hasil - pajak
baju_aksesoris = gaji_bersih * 10 / 100
alat_tulis = gaji_bersih * 1 / 100
sedekah = (gaji_bersih - baju_aksesoris - alat_tulis) * 25 / 100
sedekah_anak_yatim = (sedekah // 1000) * (30 / 100) * 1000
sedekah_kaum_dhuaafa = sedekah - sedekah_anak_yatim
sisa_uang = gaji_bersih - (baju_aksesoris + alat_tulis + sedekah)

print(f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak {hasil:,}")
print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak {gaji_bersih:,}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris {baju_aksesoris:,}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis {alat_tulis:,}")
print(f"Jumlah uang yang akan Budi sedekahkan {sedekah:,}")
print(f"Jumlah uang yang akan diterima anak yatim {sedekah_anak_yatim:,}")
print(f"Jumlah uang yang akan diterima kaum dhuafa {sedekah_kaum_dhuaafa:,}")
print(f"Sisa Uang Budi adalah {sisa_uang:,}")

