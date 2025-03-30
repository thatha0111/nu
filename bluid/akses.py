import os, json, time, sys, platform
from urllib.error import URLError
from urllib.parse import quote
from urllib import request

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'	 # WARNA MATI

class Cek_lisen:

    def __init__(self):
        self.kya = "data/cache/.lisen.txt" #/data/data/com.termux/files/home/.lisen.txt
        self.url = "https://licensi.yayanxd.my.id"
        self.admin_contact = "https://wa.me/6283890285641"

    def cek_lisen(self):
        try:
            key = open(self.kya, "r").read().strip()
        except FileNotFoundError:
            self.login_key()
        
        dev = self.cek_device()
        try:
            devc = quote(f"{dev['brand']} {dev['device']}")
            xnxx = request.urlopen(f"{self.url}/check.php?key={key}&dev={devc}")
            response_text = xnxx.read().decode('utf-8')
            asuu = json.loads(response_text)

            tod = asuu.get("usage", "unknown").replace("premium", f"{H}Premium{N}").replace("trial", f"{M}Trial{N}")
            msg = asuu.get("msg", "Tidak ada pesan dari server.")

            if asuu["status"] == "error":
                exit(f"\n[{M}×{N}] {msg}")

            elif asuu["status"] in ["kadaluarsa", "sudah kadaluarsa"]:
                print(f"\n[{M}×{N}] Lisensi Anda telah kedaluwarsa.")
                print(f"[{H}!{N}] Masa aktif lisensi berakhir pada: {M}{asuu['expired']}{N}.")
                print(f"[{H}>{N}] Untuk memperpanjang lisensi, silakan upgrade ke Premium.")
                time.sleep(3)
                os.system("xdg-open https://mykey.yayanxd.my.id/")
                exit()
            
        except KeyError:
            print(f"\n[{M}×{N}] {msg}")
            exit()
        except (json.decoder.JSONDecodeError, URLError):
            exit(f"\n[{M}×{N}] Gagal menghubungkan ke server. Periksa koneksi internet Anda atau coba lagi nanti.")

        return asuu, tod

    def cek_device(self):
        system_name = platform.system()
        os_name = os.popen("uname -o").read().strip()
        device_info = {"brand": "unknown","device": "unknown"}

        if system_name == "Windows":
            device_info["brand"] = "Windows"
            device_info["device"] = platform.node()
        elif system_name == "Darwin":
            device_info["brand"] = "Apple"
            device_info["device"] = platform.node()
        elif system_name == "Linux":
            if "Android" in os_name:
                device_info["brand"] = os.popen("getprop ro.product.manufacturer").read().strip() or "unknown"
                device_info["device"] = os.popen("getprop ro.product.marketname").read().strip() or os.popen("getprop ro.product.model").read().strip() or "unknown"
            else:
                try:
                    with open("/sys/devices/virtual/dmi/id/sys_vendor", "r") as f:
                        device_info["brand"] = f.read().strip() or "unknown"
                    with open("/sys/devices/virtual/dmi/id/product_name", "r") as f:
                        device_info["device"] = f.read().strip() or "unknown"
                except FileNotFoundError:
                    device_info["device"] = "Linux Machine"

        return device_info

    def login_key(self):
        if "win" in sys.platform:
            os.system("cls")
        else:
            os.system("clear")
        print(f"""
Hai! Selamat datang di script Yayan XD Brute, jika ingin mendapatkan API key
    silahkan daftar ke situs ini: {H}https://mykey.yayanxd.my.id{N}
         -----------------------------------------------
""")
        key = input(f"[{H}*{N}] Masukkan API key kamu: ")
        if key in [""]:
            print(f"\n[{M}×{N}] Jangan kosong")
            time.sleep(3)
            self.login_key()

        dev = self.cek_device()
        try:
            devc = quote(f"{dev['brand']} {dev['device']}")
            reso = request.urlopen(f"{self.url}/check.php?key={key}&dev={devc}")
            xnxx = json.loads(reso.read())

            if xnxx["status"] == "error":
                print(f"\n[{M}×{N}] {xnxx['msg']}")
                exit()
            elif xnxx["status"] in ["kadaluarsa", "sudah kadaluarsa"]:
                print(f"\n[{M}×{N}] Lisensi Anda telah kedaluwarsa.")
                print(f"[{H}!{N}] Masa aktif lisensi berakhir pada: {M}{xnxx['expired']}{N}.")
                print(f"[{H}>{N}] Untuk memperpanjang lisensi, silakan upgrade ke Premium.")
                time.sleep(3)
                os.system("xdg-open https://mykey.yayanxd.my.id/")
                exit()

            else:
                kadaluarsa = xnxx["expired"]
                user = xnxx["nama"]
                open(self.kya, "w").write(key)

                print(f"""\n👋 Hello {H}{user}!{N}  
🔑 API key Anda masih aktif dan berlaku hingga: {M}{kadaluarsa}{N}  
✅ Gunakan tools ini dengan bijak dan manfaatkan sebaik mungkin! 😊""")

                time.sleep(2)
                exit(f"\n[{M}➡{N}] Silakan jalankan ulang perintah dengan mengetik: {H}python run.py{N}")

        except URLError:
            print(f"\n[{M}×{N}] Gagal menghubungkan ke server, silahkan cek koneksi Anda dan aktifkan mode pesawat 5 detik.")
            exit()