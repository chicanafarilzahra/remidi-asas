# fungsi untuk menghitung biaya parkir
def hitung_biaya_parkir(durasi):
    # tarif parkir
    dua_jam_pertama= 3000
    lebih_dari_2_jam= 1500
    biaya_tambahan= 10000

    # hitung biaya dasar
    if durasi <=2:
        biaya= dua_jam_pertama
    else:
        biaya = dua_jam_pertama + (durasi - 2) * lebih_dari_2_jam

    # Tambahkan biaya tambahan jika durasi lebih dari 24 jam
    if durasi >24:
        biaya += biaya_tambahan

    return biaya

try:
    # input dari pengguna
    durasi= int(input("masukkan durasi:"))

    # Validasi durasi
    if durasi <0:
        print("durasi anda tidak valid.")
    else:
        # hitung biaya parkir
        biaya= hitung_biaya_parkir(durasi)
        print(f"biaya parkir untuk {durasi} jam adalah Rp{biaya}")
except ValueError:
    # tangani input yang bukan angka
    print("harap masukkan durasi yang valid (dalam angka).")