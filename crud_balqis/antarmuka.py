from crud.lihat import lihat
from crud.create import create_record
from crud.update import update_record
from crud.delete import delete_record

def main():
    while True:
        print("\nMODIFIKASI DATABASE")
        print("-----------------------------------------")
        print("1. CREATE")
        print("2. READ")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. EXIT")
        print("-----------------------------------------")

        pil = int(input("MASUKKAN PILIHAN: "))

        if pil == 1:
            id = int(input("Masukkan  id: "))
            nama = input("masukan nama kamu: ")
            jenis_kel = input("Masukkan jenis kelamin: ")
            create_record( id, nama, jenis_kel )
            print("Data berhasil ditambahkan.")
            lihat()
        elif pil == 2:
            lihat()
        elif pil == 3:
            id = int(input("Masukkan ID: "))
            nama = input("Masukkan nama baru: ")
            jenis_kel = input("Masukkan jenis kelamin kamu: ")
            update_record(id, nama, jenis_kel)
            print("Data berhasil diupdate.")
            lihat()
        elif pil == 4:
            id = int(input("Masukkan ID yang mau dihapus: "))
            delete_record(id)
            print("Data berhasil dihapus.")
            lihat()
        elif pil == 5:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak ada. Silakan coba lagi.")

if __name__ == "__main__":
    main()