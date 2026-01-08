import random

# --- 1. Fungsi Pengecek Bilangan Prima ---
def apakah_prima(n):
    """Memeriksa apakah bilangan n adalah bilangan prima."""
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# --- 2. Fungsi Utama Permainan ---
def main_game_tebak_prima():
    print("✨ Selamat Datang di Permainan Tebak Bilangan Prima! ✨")
    print("-------------------------------------------------------")

    # Tentukan rentang permainan
    BATAS_BAWAH = 2
    BATAS_ATAS = 100

    # Kumpulkan semua bilangan prima dalam rentang
    daftar_prima = []
    for num in range(BATAS_BAWAH, BATAS_ATAS + 1):
        if apakah_prima(num):
            daftar_prima.append(num)

    # Pilih bilangan prima rahasia secara acak
    if not daftar_prima:
        print("Error: Tidak ada bilangan prima dalam rentang yang ditentukan.")
        return

    bilangan_rahasia = random.choice(daftar_prima)

    print(f"Saya telah memilih bilangan prima antara {BATAS_BAWAH} dan {BATAS_ATAS}.")
    print("Coba tebak bilangan tersebut!")

    batas_percobaan = 7
    percobaan = 0

    while percobaan < batas_percobaan:
        try:
            tebakan = int(input(f"\nKesempatan ke-{percobaan + 1}/{batas_percobaan}. Masukkan tebakan Anda: "))
            percobaan += 1

            if tebakan == bilangan_rahasia:
                print(f"\n🎉 SELAMAT! Anda berhasil menebak bilangan prima {bilangan_rahasia} dalam {percobaan} kali percobaan.")
                return

            elif tebakan < bilangan_rahasia:
                print("Terlalu kecil! Coba angka yang lebih besar.")
            else:
                print("Terlalu besar! Coba angka yang lebih kecil.")

            if not apakah_prima(tebakan):
                print("Petunjuk: Angka yang Anda tebak BUKAN bilangan prima.")

        except ValueError:
            print("Input tidak valid. Masukkan hanya angka bulat.")

    # Jika percobaan habis
    print(f"\n❌ MAAF, kesempatan Anda telah habis.")
    print(f"Bilangan prima rahasia adalah {bilangan_rahasia}.")

# Panggil fungsi utama untuk memulai permainan
if __name__ == "__main__":
    main_game_tebak_prima()
