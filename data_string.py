# a = 10
# b = 15
# if a > b:
#     print("A lebih besar dari B")
# else:
#     print("A lebih kecil dari B")

# for x in range(10):
#     print(x + 1)

# a = "tomat murah"
# b = "tomat_merah_tidak_murah"
# if not a > b: 
#     print("a jawaban tidak benar, yang benar b")


tomat_warna = "hijau"
warna_merah_murah = False

tomat_itu_murah = False
tomat_merah_itu_tidak_murah = True

if tomat_warna == "merah":
    tomat_itu_murah = warna_merah_murah

if tomat_warna == "merah" and warna_merah_murah == False :
    tomat_merah_itu_tidak_murah = True
    
else:
    tomat_merah_itu_tidak_murah = False

print("tomat itu murah:",tomat_itu_murah)
print("yang warna merah itu tidak murah", tomat_merah_itu_tidak_murah)