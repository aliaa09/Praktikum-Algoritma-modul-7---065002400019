def tentukan_akhiran_ordinal(angka):
    """
    Fungsi untuk menentukan format ordinal dari suatu angka.
    """
    if 11 <= angka % 100 <= 13:
        akhiran = "th"
    else:
        digit_terakhir = angka % 10
        if digit_terakhir == 1:
            akhiran = "st"
        elif digit_terakhir == 2:
            akhiran = "nd"
        elif digit_terakhir == 3:
            akhiran = "rd"
        else:
            akhiran = "th"
    return akhiran


def main():
    """
    Program utama untuk meminta input dari pengguna dan menampilkan hasil.
    """
    print("Ordinal Number")
    print("ketik 0 untuk menghentikan program")

    while True:
        try:
            masukan = int(input("masukkan angka: "))
            akhiran = tentukan_akhiran_ordinal(masukan)
            print(f"({masukan}, '{akhiran}')")
            if masukan == 0:
                print("terima kasih telah menggunakan program saya")
                break
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    main()
