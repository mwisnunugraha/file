# print(
# """   
# PENJUMLAHAN = +
# PENGURANGAN = -
# KELUAR PROGRAM = exit
# """
# )


def pertambahan(angka1, angka2):
    return angka1 + angka2

if __name__ == "__main__":
    fungsi_kalkulator = {
        1: pertambahan
    }

    print("""
    Selamat datang di kalkulator sederhana.
    masukkan operasi yang diinginkan:
    1. tambah
    """)

    user_input = int(input("Masukkan operasi yang anda inginkan: "))

    if user_input not in fungsi_kalkulator:
        print("invalid input")
        exit()

    angka1 = int(input("masukkan angka 1: "))
    angka2 = int(input("masukkan angka 2: "))
    hasil = fungsi_kalkulator[user_input](angka1, angka2)
    print ("Hasil : ",hasil)



# while True:
#     try:
#         masukanPerintah = eval(input("Masukan perintah"))
#         print(f"Hasil : {masukanPerintah}")
#     except Exception as e:
#             print("Input yang benar")