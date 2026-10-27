# ==================================================================================
#Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : GILBERT ARMANDO GULTOM
# NIM   : 613260006
# Kelas : 11 D3 TI
# ==================================================================================

print("===================================")
print("Program Penentuan Grade dan Kelulusan")
print("===================================")

nilai1 =float(input("Masukkan nilai pertama (0-100): "))
nilai2 =float(input("Masukkan nilai kedua (0-100): "))
nilai3 = (nilai1 + nilai2)/2
if nilai3 >= 90:
    Grade = "A"
    Kelulusan = "lulus"
    if nilai3 >= 100:
            print("Nilai yang dimasukkan tidak valid.")
    else:
        print(f"nilai akhir kamu {nilai3} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
elif nilai3 >= 80:
    Grade = "B"
    Kelulusan = "lulus"
    print(f"nilai akhir kamu {nilai3} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
elif nilai3 >= 70:
    Grade = "C"
    Kelulusan = "lulus bersyarat"
    print(f"nilai akhir kamu {nilai3} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
elif nilai3 >= 60:
    Grade = "D"
    Kelulusan = "tidak lulus"
    print(f"nilai akhir kamu {nilai3} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
elif nilai3 >= 50:
    Grade = "E"
    Kelulusan = "tidak lulus"
    if nilai3 >= 0:
        print("Nilai yang dimasukkan tidak valid.")
    else:
        print(f"nilai akhir kamu {nilai3} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
else:
    print("Nilai yang dimasukkan tidak valid. Silakan masukkan nilai antara 0 hingga 100.")

print("===================================")
print("Terima kasih telah menggunakan program ini.")
print("===================================")