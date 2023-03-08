print(
"""   
PENJUMLAHAN = +
PENGURANGAN = -
KELUAR PROGRAM = exit
"""
)

while True:
    try:
        masukanPerintah = eval(input("Masukan perintah"))
        print(f"Hasil : {masukanPerintah}")
    except Exception as e:
            print("Input yang benar")