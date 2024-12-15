# fungsi untuk menghitung biaya pengiriman paket
def hitung_biaya_paket(dimensi, berat, lokasi):
    # lokasi yang valid
    lokasi_valid= ["kota pasuruan", "kabupaten pasuruan"]
    # validasi lokasi pengiriman
    if lokasi.lower() not in lokasi_valid:
        return -1, "lokasi tidak valid."
    
    # memecah dimensi menjadi panjang, lebar, tinggi
    panjang, lebar, tinggi= dimensi

    # validasi dimensi tidak boleh negatif/nol
    if panjang <= 0 or lebar <=0 or tinggi <=0:
        return -1, "dimensi paket tidak valid."
    
    # menghitung volume paket
    volume= panjang * lebar * tinggi
    # menentukan berat minimal 1 kg
    berat= max(berat, 1)

    # menentukan biaya berdasarkan volume & berat
    if volume <= 50*50*50:
        biaya= berat * 5000 # paket kecil
    else:
        biaya= 50000 + berat * 7000 # paket besar

    # biaya minimal adalah Rp.8000
    return max(biaya, 8000), "biaya berhasil dihitung."

# input dari pengguna
try:
    # meminta pengguna masukkan panjang paket
    panjang= int(input("masukkan panjang paket(cm):"))
    # lebar paket
    lebar= int(input("masukkan lebar paket(cm):"))
    # tinggi paket
    tinggi= int(input("masukkan tinggi paket(cm):"))
    # berat paket
    berat= float(input("masukkan berat paket(kg):"))

    # validasi berat paket harus lebih dari 0
    if berat <= 0:
        print("berat paket harus lebih dari 0.")
    else:
        # meminta pengguna memasukkan lokasi
        lokasi= input("masukkan lokasi pengiriman:.").strip()
        # menyusun dimensi sebagai tuple
        dimensi= (panjang, lebar, tinggi)
        # memanggil fungsi untuk biaya paket
        total_biaya, pesan= hitung_biaya_paket(dimensi, berat, lokasi)

        # mengecek apakah lokasi tidak valid
        if total_biaya == -1:
            print(pesan)
        else:
            # menampilkan pesan keberhasilan dan total biaya
            print(f"{pesan} total biaya paket anda adalah Rp{total_biaya:,.0f}")
            print(f"{pesan} paket anda akan dikirim.")
except ValueError:
    # menangani apabila input tidak valid
    print("input tidak valid. pastikan memasukkan angka untuk dimensi dan berat.")