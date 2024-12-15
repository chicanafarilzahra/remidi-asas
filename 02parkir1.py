# fungsi menghitung biaya parkir
def hitung_biaya_parkir(durasi, kendaraan):
    # menentukan tarif berdasarkan jenis kendaraan
    if kendaraan == "motor":
        tarif_awal= 3000
        tarif_per_jam= 1000
    elif kendaraan == "mobil":
        tarif_awal= 3000
        tarif_per_jam= 1500
    else:
        # Mengembalikan pesan error jika jenis kendaraan tidak valid
        return "jenis kendaraan tidak valid"
    
    # tarif tambahan jika durasi lebih 24 jam
    tarif_tambahan_24_jam= 10000

    # Menghitung biaya parkir berdasarkan durasi
    if durasi <=2:
        biaya= tarif_awal
    elif durasi <=24:
        biaya=tarif_awal + (durasi-2) * tarif_per_jam
    else:
        biaya= tarif_awal +(durasi-2) * tarif_per_jam + tarif_tambahan_24_jam

    # Mengembalikan biaya parkir yang telah dihitung
    return round(biaya)
    
# Input dari pengguna untuk jenis kendaraan
kendaraan= input("Masukkan jenis kendaraan(motor/mobil):").strip().lower()

# Validasi jenis kendaraan
if kendaraan not in["motor", "mobil"]:
    print("maaf, parkir hanya untuk motor dan mobil.")
else:
    # Input dari pengguna untuk durasi parkir
    jumlah_durasi= input("masukkan durasi parkir:").strip()

    # Validasi apakah input durasi adalah angka
    if jumlah_durasi.isdigit():
        jumlah_durasi= int(jumlah_durasi)

        # Validasi apakah durasi lebih besar dari 0
        if jumlah_durasi <=0:
            print("maaf, durasi tidak boleh nol/negatif.")
        else:
            # Menghitung biaya parkir menggunakan fungsi
            biaya= hitung_biaya_parkir(jumlah_durasi, kendaraan)
            print(f"Biaya parkir untuk{kendaraan} selama {jumlah_durasi} jam adalah Rp{biaya:,}")
    else:
        # Pesan error jika durasi bukan angka valid
        print("masukkan angka yang valid untuk jam parkir.")