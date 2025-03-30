import os, re, time
from .post import ASU
from .komen import ABC
from bluid.logo import Logo

H = "\x1b[0;32m"  # Hijau
M = "\x1b[0;31m"  # Merah
N = "\x1b[0m"     # Reset ke default

class Main:

    def __init__(self, lim, asw):
        self.lim = lim
        self.asw = asw
        self.fil = "botfb/data/"


    def main_menu(self):
        while True:
            Logo("bot_fb")
            print(self.asw)
            print(f"[{H}1{N}] Komen Fb\n[{H}2{N}] Post Ke Grup\n[{H}3{N}] Tambah atau Hapus akun tumbal\n[{H}0{N}] kembali ke menu")
            print("-" * 50)
            pilihan = input(" ?. Pilih (nomor): ").strip()
            if pilihan in ["01", "1"]:
                self.mulai("komen_fb")
            elif pilihan in ["02", "2"]:
                self.mulai("post_grup")
            elif pilihan in ["03", "3"]:
                self.tambah_dan_hapus()
            elif pilihan in ["00", "0"]:
                return
            else:
                print(f"\n {M}!{N}. Input yang bener.")
                time.sleep(1)


    def tampilkan_file(self):
        try:
            files = sorted(os.listdir(self.fil))
        except Exception:
            exit(f"\n {M}!{N}. Tidak ada file di folder!")
        
        if not files:
            exit(f"\n {M}!{N}. Tidak ada file di folder!")
        
        print("-" * 50)
        for i, file in enumerate(files, start=1):
            print(f" {H}{i:02}{N}. {file}")
        print(f" {M}00{N}. Kembali ke folder utama.")
        print("-" * 50)
        return files

    def mulai(self, abcd):
            while True:
                Logo("bot_fb")
                print(self.asw)
                files = self.tampilkan_file()
                file_input = input(" ?. Pilih file (nomor): ").strip()
                if file_input in ["0", "00"]:
                    break
                if not file_input.isdigit() or int(file_input) < 1 or int(file_input) > len(files):
                    print(f"\n {M}!{N}. Pilihan file tidak valid! Coba lagi.")
                    time.sleep(1)
                    continue
                file_name = files[int(file_input) - 1]
                print()
                print("-" * 50)
                print(f">> Anda memilih file: {file_name}")
                print("-" * 50)
                try:
                    with open(f"{self.fil}{file_name}", "r") as f:
                        content = f.read()
                    user = re.findall(r"c_user=(\d+)", content)
                    if user:
                        if "komen_fb" in abcd:
                            ABC(content.strip(), user[0]).komen_fsnk()
                        elif "post_grup" in abcd:
                            ASU(content.strip(), user[0]).postt_grup()
                    else:
                        print("\n>> Tidak ada ID pengguna dalam file!")
                except Exception as e:
                    print(f"Error membaca file: {e}")
                return

    def tambah_dan_hapus(self):
        while True:
            print("\n[1] Tambah akun")
            print("[2] Hapus akun")
            print("[3] kembali")
            pilihan = input("\n[>] Pilih menu: ").strip()
            if pilihan == "1":
                self.tambah_akun()
            elif pilihan == "2":
                self.hapus_akun()
            elif pilihan == "3":
                return
            else:
                print("[!] Pilihan tidak valid, coba lagi.")


    def tambah_akun(self):
        while True:
            print("\n[!] Masukkan nama akun tumbal:")
            file = input("[?] Nama akun: ").strip()
            if not file:
                print("[!] Nama akun tidak boleh kosong!")
                continue

            print("\n[!] Masukkan cookie akun tumbal:")
            cookie = input("[?] Cookie akun: ").strip()
            if not cookie:
                print("[!] Cookie akun tidak boleh kosong!")
                continue

            self.save_hasil(file, cookie)
            tanya = input("\n[?] Tambah lagi akun tumbal (Y/t): ").strip().lower()
            if tanya == "t":
                self.main_menu()


    def save_hasil(self, filename, data):
        path = f"{self.fil}{filename}.txt"
        with open(path, "a") as file:
            file.write(data + "\n")
        print(f"[+] Akun '{H}{filename}{N}' berhasil ditambahkan ke {H}{path}{N}")


    def hapus_akun(self):
        files = [f for f in os.listdir(self.fil) if f.endswith(".txt")]
        if not files:
            print("[!] Tidak ada akun yang tersimpan.")
            return

        print("\n[!] Daftar akun tumbal:")
        file_map = {}
        for i, file in enumerate(files, start=1):
            akun_nama = file.replace(".txt", "")
            file_map[i] = file
            print(f"[{i}] {akun_nama}")

        pilihan = input(f"\n[?] Hapus akun yang mana? (contoh: 1,3,4): ").strip()
        try:
            pilihan_list = [int(x) for x in pilihan.replace(",", " ").split()]
            akun_terhapus = []
            for nomor in pilihan_list:
                if nomor in file_map:
                    akun_dihapus = file_map[nomor]
                    os.remove(os.path.join(self.fil, akun_dihapus))
                    akun_terhapus.append(akun_dihapus.replace(".txt", ""))

            if akun_terhapus:
                print(f"[+] Akun yang berhasil dihapus: {', '.join(akun_terhapus)}")
            else:
                print("[!] Tidak ada akun yang dihapus.")

        except ValueError:
            print("[!] Masukkan angka yang benar.")